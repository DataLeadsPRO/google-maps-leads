import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Google Maps Leads API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "maps_search",
    "method": "POST",
    "path": "/maps/search",
    "description": "V1 Maps Search"
  },
  {
    "name": "maps_status",
    "method": "POST",
    "path": "/maps/status",
    "description": "V1 Maps Status"
  },
  {
    "name": "maps_results",
    "method": "POST",
    "path": "/maps/results",
    "description": "V1 Maps Results"
  },
  {
    "name": "maps_jobs",
    "method": "POST",
    "path": "/maps/jobs",
    "description": "V1 Maps Jobs"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
