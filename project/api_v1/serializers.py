from pydantic import BaseModel, validator, ValidationError
from uuid import UUID


def not_negative(value) -> int:
    if value < 0:
        raise ValidationError('Not negative value')
    return value


class SubstructBalanceSerializer(BaseModel):
    uuid: UUID
    substraction: int

    @classmethod
    @validator('substraction')
    def not_negative_value(cls, value: int) -> int:
        return not_negative(value)


class AddBalanceSerializer(BaseModel):
    uuid: UUID
    amount: int

    @classmethod
    @validator('amount')
    def not_negative_value(cls, value: int) -> int:
        return not_negative(value)


class GetStatusSerializer(BaseModel):
    uuid: UUID
    