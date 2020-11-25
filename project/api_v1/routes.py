from starlette.routing import Route

from .views import (account_status_view, add_balance_view, ping_view,
                    substruct_balance_view)

routes = [
    Route('/ping', endpoint=ping_view, methods=['GET']),
    Route('/substract', endpoint=substruct_balance_view, methods=['POST', 'PATCH', 'PUT']),
    Route('/add', endpoint=add_balance_view, methods=['POST', 'PATCH', 'PUT']),
    Route('/status', endpoint=account_status_view, methods=['POST', 'PATCH', 'PUT']),
]
