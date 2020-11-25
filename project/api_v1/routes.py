from starlette.routing import Route

from .views import ping_view


routes = [
    Route('/ping', endpoint=ping_view, methods=['GET']),
]
