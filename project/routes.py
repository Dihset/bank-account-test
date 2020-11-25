from starlette.routing import Mount

from .api_v1.routes import routes


routes = [
    Mount('/api/v1', routes=routes)
]
