from __future__ import annotations

import asyncio
from typing import Dict, Union
from uuid import uuid4

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.transactions import atomic

from .models import Account

AccountPyDantic = pydantic_model_creator(Account)


class PostgresAccountRepository:
    
    @classmethod
    async def get_by_uuid(cls, uuid: Union[str, uuid4]) -> AccountPyDantic:
        account = await Account.get(uuid=uuid, is_open=True)
        return await AccountPyDantic.from_tortoise_orm(account)
    
    @classmethod
    async def substract_balance(cls, uuid: Union[str, uuid4], substraction: int) -> AccountPyDantic:
        account = await Account.get(uuid=uuid, is_open=True)
        result = account.balance - account.holds - substraction
        if result < 0:
            raise Exception()
        account.holds += substraction
        await account.save()
        return await AccountPyDantic.from_tortoise_orm(account)

    @classmethod
    async def add_balance(cls, uuid: Union[str, uuid4], amount: int) -> AccountPyDantic:
        account = await Account.get(uuid=uuid, is_open=True)
        account.balance += amount
        await account.save()
        return await AccountPyDantic.from_tortoise_orm(account)
    
    @classmethod
    async def clear_holds(cls) -> None:
        connection = Tortoise.get_connection("default")
        sql = '''
            UPDATE account
            SET balance = balance - holds,
                holds = 0
            WHERE holds > 0
              AND is_open = TRUE
        '''
        await connection.execute_query(sql)
