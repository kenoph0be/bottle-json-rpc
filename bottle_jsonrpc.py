#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple JSON-RPC extension for the Bottle micro-framework.
Copyright (c) 2015, Paolo Montesel.
License: MIT (see LICENSE for details)
"""

import bottle
import json


__author__ = 'Paolo Montesel'
__version__ = '0.1-dev'
__license__ = 'MIT'


class RpcNoSuchMethodException(Exception):
    pass


class RpcJsonParseError(Exception):
    pass


class RpcInvalidParametersException(Exception):
    pass


class RpcInvalidRequestException(Exception):
    pass


class EndPoint():
    def __init__(self, path, http_method="POST"):
        self.http_method = http_method
        self.methods = dict()
        self.methods_args = dict()
        self.path = path

        # Register the URL
        @bottle.route(path, http_method)
        def callback():
            return self.handle_request()

    def __call__(self, method, *params):
        def decorator(decorated_func):
            self.methods[method] = decorated_func
            self.methods_args[method] = params
            return decorated_func
        return decorator

    def call_method(self, method, params, call_id, jsonrpc_ver):
        if method not in self.methods:
            raise RpcNoSuchMethodException()

        arg_names = self.methods_args[method]
        args = list()

        if type(params) == list:
            args = params
        else:
            # the parameters are named (in a dict)
            for arg_name in arg_names:
                args.append(params[arg_name] if arg_name in params else None)

        try:
            return self.methods[method](*args)
        except TypeError:
            raise RpcInvalidParametersException

    def handle_request(self):
        response = dict()
        response['jsonrpc'] = '2.0'

        try:
            data = None
            if self.http_method == "GET":
                data = bottle.request.params
            elif self.http_method == "POST":
                try:
                    data = json.load(bottle.request.body)
                except:
                    raise RpcJsonParseError
            else:
                raise Exception("Invalid HTTP Method!")

            call_id = data['id'] if 'id' in data else None
            jsonrpc_ver = data['jsonrpc'] if 'jsonrpc' in data else '2.0'

            method = None
            if 'method' in data:
                method = data['method']
            else:
                raise RpcInvalidRequestException

            # call_id is None in case of JSON-RPC notification (which implies an empty response body from the server)
            if call_id is not None:
                response['id'] = call_id

            params = None
            if self.http_method == "GET":
                try:
                    params = json.loads(data['params']) if 'params' in data else []
                except ValueError:
                    raise RpcJsonParseError
            else:
                params = data['params'] if 'params' in data else []

            # TODO: enforce no output if 'id' is None?
            response['result'] = self.call_method(method, params, call_id, jsonrpc_ver)

            if call_id is None:
                return ""

        except RpcNoSuchMethodException:
            response['error'] = self.make_error(-32601, 'Method not found')
        except RpcJsonParseError:
            response['error'] = self.make_error(-32700, 'Parse error')
        except RpcInvalidRequestException:
            response['error'] = self.make_error(-32600, 'Invalid Request')
        except RpcInvalidParametersException:
            response['error'] = self.make_error(-32602, 'Invalid params')

        return response

    def make_error(self, code, message):
        return {'code': code, 'message': message}
