from project.core.repositories import \
    PostgresAccountRepository as AccountRepository
from project.utils import CustomJSONResponse as JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request


async def ping_view(request: Request) -> JSONResponse:
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": {},
        "description": {}
    })


async def substruct_balance_view(request: Request) -> JSONResponse:
    data = await request.json()
    account = await AccountRepository.substract_balance(
        uuid=data['uuid'],
        substraction=int(data['substraction']),
    )
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": account.dict(),
        "description": {}
    })


async def add_balance_view(request: Request) -> JSONResponse:
    data = await request.json()
    account = await AccountRepository.add_balance(
        uuid=data['uuid'],
        amount=int(data['amount']),
    )
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": account.dict(),
        "description": {}
    })


async def account_status_view(request: Request) -> JSONResponse:
    data = await request.json()
    account = await AccountRepository.get_by_uuid(
        uuid=data['uuid']
    )
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": account.dict(),
        "description": {}
    })
