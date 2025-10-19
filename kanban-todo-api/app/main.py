"""Shim to expose the ASGI `app` object as `app.main:app`.

Some deployment tools call `uvicorn app.main:app` — this module imports the
application instance defined in the project root `main.py` to match that.
"""

from importlib import import_module

# Import the project root main module and expose its `app` variable
_root_main = import_module("main")
app = getattr(_root_main, "app")
