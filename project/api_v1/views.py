from project.core.repositories import \
    PostgresAccountRepository as AccountRepository
from project.utils import CustomJSONResponse as JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request

from .serializers import (AddBalanceSerializer, GetStatusSerializer,
                          SubstructBalanceSerializer)


async def ping_view(request: Request) -> JSONResponse:
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": {},
        "description": {}
    })


async def substruct_balance_view(request: Request) -> JSONResponse:
    data = await request.json()
    valid_data = SubstructBalanceSerializer(**data)
    account = await AccountRepository.substract_balance(
        uuid=valid_data.uuid,
        substraction=valid_data.substraction,
    )
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": account.dict(),
        "description": {}
    })


async def add_balance_view(request: Request) -> JSONResponse:
    data = await request.json()
    valid_data = AddBalanceSerializer(**data)
    account = await AccountRepository.add_balance(
        uuid=valid_data.uuid,
        amount=valid_data.amount,
    )
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": account.dict(),
        "description": {}
    })


async def account_status_view(request: Request) -> JSONResponse:
    data = await request.json()
    valid_data = GetStatusSerializer(**data)
    account = await AccountRepository.get_by_uuid(
        uuid=valid_data.uuid
    )
    return JSONResponse({
        "status": 200,
        "result": True,
        "addition": account.dict(),
        "description": {}
    })
