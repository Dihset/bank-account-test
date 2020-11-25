import asyncio
import logging

from starlette.applications import Starlette
from .middlewares import middlewares


logger = logging.getLogger(__name__)


def init_app(*args, **kwargs):
    logger.info('init starlette')
    app = Starlette(
        debug=True,
        middleware=middlewares
    )
    logger.info('starlette application inited')
    return app
