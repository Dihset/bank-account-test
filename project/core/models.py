from tortoise import fields, models


class Account(models.Model):
    uuid = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=20)
    balance = fields.IntField(default=0)
    holds = fields.IntField(default=0)
    is_open = fields.BooleanField(index=True, default=True)
