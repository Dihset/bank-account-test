import asyncio
import logging

from starlette.applications import Starlette
from tortoise.contrib.starlette import register_tortoise

from .middlewares import middlewares
from .routes import routes
from .settings import DB_URI

logger = logging.getLogger(__name__)


def init_app(*args, **kwargs):
    logger.info('init starlette')
    app = Starlette(
        debug=True,
        routes=routes,
        middleware=middlewares
    )
    register_tortoise(
        app,
        config={
            'connections': {
                'default': DB_URI
            },
            'apps': {
                'models': {
                    'models': ['project.core.models'],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True
    )
    logger.info('starlette application inited')
    return app
