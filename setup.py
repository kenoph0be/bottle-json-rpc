#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use bottle.")

import bottle_jsonrpc

setup(
    name='bottle_jsonrpc',
    version=bottle_jsonrpc.__version__,
    description='JSON-RPC extension for the bottle micro-framework.',
    long_description=bottle_jsonrpc.__doc__,
    author=bottle_jsonrpc.__author__,
    author_email='paolo.montesel{[AT]}gmail.com',
    # url='http://site.com/',
    py_modules=['bottle_jsonrpc'],
    scripts=['bottle_jsonrpc.py'],
    license='MIT',
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires=["bottle"]
)
