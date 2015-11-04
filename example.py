#!/usr/bin/env python

"""
Test sum:   curl -g "http://127.0.0.1:8080/api" --data '{"method": "sum", "params": [1,2,3], "id": 1}'; echo
Output:     {"jsonrpc": "2.0", "id": 1, "result": 6}
Test mul 1: curl -g "http://127.0.0.1:8080/api" --data '{"method": "mul", "params": {"a":-1,"b":7}, "id": 1}'; echo
Output:     {"jsonrpc": "2.0", "id": 1, "result": -7}
Test mul 2: curl -g "http://127.0.0.1:8080/api" --data '{"method": "mul", "params": [-1,7], "id": 1}'; echo
Output:     {"jsonrpc": "2.0", "id": 1, "result": -7}
"""

from bottle import run

import bottle_jsonrpc as jsonrpc
# Looks better but causes troubles to PyCharm analysis because it's magic :(
#import bottle.ext.jsonrpc as jsonrpc


# Create the end-point and return an annotation for mapping methods to it
api = jsonrpc.EndPoint('/api')


# Unnamed parameters get passed automatically to the decorated function
@api('sum')
def rpc_sum(*args):
    return sum(args)


# Auto-mapping of named parameters
@api('mul', 'a', 'b')
def rpc_mul(a, b):
    if a is None or b is None:
        raise jsonrpc.RpcInvalidParametersException
    return a * b

if __name__ == '__main__':
    run(port=8080, reloader=True)
