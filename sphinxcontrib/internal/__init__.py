from docutils import nodes
from docutils.parsers.rst import Directive

import sphinx
from sphinx.util.nodes import set_source_info

if False:
    # For type annotation
    from typing import Any, Dict, List  # NOQA
    from sphinx.application import Sphinx  # NOQA


class internal(nodes.Element):
    pass


class Internal(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}  # type: Dict

    def run(self):
        # type: () -> List[nodes.Node]
        node = internal()
        node.document = self.state.document
        set_source_info(self, node)
        self.state.nested_parse(self.content, self.content_offset,
                                node, match_titles=1)
        return [node]

from docutils.parsers.rst.directives import admonitions

def process_internal_nodes(app, doctree, docname):
    # type: (Sphinx, nodes.Node, unicode) -> None
    ns = dict((confval.name, confval.value) for confval in app.config)
    ns.update(app.config.__dict__.copy())
    ns['builder'] = app.builder.name
    show = False
    if app.builder.name == 'html' and ('show_internal_html' in app.config) and app.config.show_internal_html:
        show = True
    elif 'internal' in app.tags:
        show = True

    for node in doctree.traverse(internal):
        if show:
            admonition = nodes.admonition(node.rawsource, *node.children, **node.attributes)
            title = nodes.title('', 'Internal')
            admonition.insert(0, title)
            admonition['classes'].append('error')
            admonition['classes'].append('internal')
            node.replace_self(admonition)
        else:
            node.replace_self([])


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_node(internal)
    app.add_directive('internal', Internal)
    app.add_config_value('show_internal_html', True, True)
    app.connect('doctree-resolved', process_internal_nodes)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
