import asyncio

import uvicorn

from project import init_app
from project.settings import *


if __name__ == '__main__':
    uvicorn.run(
        app=init_app(),
        host='0.0.0.0',
        port=8080,
        log_level="debug",
        debug=True,
        loop='asyncio',
    )