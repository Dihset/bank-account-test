from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint


async def ping_view(request: Request) -> JSONResponse:
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": {},
        "description": {}
    })


async def substruct_balance_view(request: Request) -> JSONResponse:
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": {},
        "description": {}
    })


async def add_balance_view(request: Request) -> JSONResponse:
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": {},
        "description": {}
    })

class BalanceStatusView(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        return JSONResponse({
            "status": 200,
            "result": True,
            "addition": {},
            "description": {}
        })
    
    async def patch(self, request: Request) -> JSONResponse:
        return JSONResponse({
            "status": 200,
            "result": True,
            "addition": {},
            "description": {}
        })