============================
Bottle JSON-RPC Extension
============================

Simple JSON-RPC extension for the Bottle micro-framework.


Example: "Sum" JSON-RPC
----------------------------------

.. code-block:: python

    from bottle import run

    # import bottle_jsonrpc as jsonrpc
    import bottle.ext.jsonrpc as jsonrpc


    # Create the end-point and return an annotation for mapping methods to it
    api = jsonrpc.EndPoint('/api')


    # Unnamed parameters get passed automatically to the decorated function
    @api('sum')
    def rpc_sum(*args):
        return sum(args)

    if __name__ == '__main__':
        run(port=8080, reloader=True)

Run this script or paste it into a Python console, then use `curl` to test it:

.. code-block:: python

    curl -g "http://127.0.0.1:8080/api" --data '{"method": "sum", "params": [1,2,3], "id": 1}'

License
-------

Code and documentation are available according to the MIT License (see LICENSE).
