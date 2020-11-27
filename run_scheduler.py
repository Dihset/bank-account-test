#!/usr/bin/env python
import asyncio

from project import init_sceduler_app
from project.settings import *


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(init_sceduler_app())
    loop.run_forever()
