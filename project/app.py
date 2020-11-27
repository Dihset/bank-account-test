import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from starlette.applications import Starlette
from tortoise import Tortoise
from tortoise.contrib.starlette import register_tortoise

from .core.repositories import PostgresAccountRepository
from .middlewares import middlewares
from .routes import routes
from .settings import TORTOISE_CONFIG

logger = logging.getLogger(__name__)


def init_web_app(*args, **kwargs) -> Starlette:
    logger.info('init starlette')
    app = Starlette(
        debug=True,
        routes=routes,
        middleware=middlewares
    )
    register_tortoise(
        app,
        config=TORTOISE_CONFIG,
        generate_schemas=True
    )
    logger.info('starlette application inited')
    return app


async def init_sceduler_app(*args, **kwargs) -> AsyncIOScheduler:
    await Tortoise.init(config=TORTOISE_CONFIG)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        PostgresAccountRepository.clear_holds, 
        'interval', 
        seconds=300
    )
    scheduler.start()
    return scheduler
    
