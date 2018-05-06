# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = ['Sphinx>=1.5']

setup(
    name='sphinxcontrib-internal',
    version='0.1',
    url='https://github.com/antmicro/sphinxcontrib-internal',
    license='BSD',
    author='Michael Gielda',
    author_email='mgielda@antmicro.com',
    description='Sphinx "internal" extension',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
