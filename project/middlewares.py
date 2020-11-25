from typing import Callable

from pydantic import ValidationError
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.requests import Request
from starlette.responses import Response
from tortoise.exceptions import OperationalError

from project.core.errors import AccountException

from .utils import CustomJSONResponse as JSONResponse


class ErrorMiddleware(BaseHTTPMiddleware):

    def _build_response(self, message: str, status_code: int) -> Response:
        return JSONResponse({
            'status': status_code,
            'result': False,
            'addition': {},
            'description': {
                'error': message
            }
        }, status_code=status_code)
    
    async def dispatch(self, request: Request, call_next: Callable[[Request], Response]) -> Response:
        try:
            return await call_next(request)
        except AccountException as error:
            return self._build_response(error.message, error.status_code)
        except OperationalError as error:
            return self._build_response(str(error), 400)
        except ValidationError as error:
            return self._build_response(error.errors(), 400)


middlewares = [
    Middleware(TrustedHostMiddleware, allowed_hosts=['*']),
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*']),
    Middleware(ErrorMiddleware)
]


