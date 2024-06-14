from datetime import datetime
from typing import Optional, Iterable

from tortoise import fields, models, Tortoise, BaseDBAsyncClient


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, null=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, null=True)
    id_telegram = fields.CharField(max_length=255)
    is_vip = fields.BooleanField(null=True)
    date_vip = fields.DatetimeField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    file_path = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"

    async def save(self, *args, **kwargs) -> None:
        if self.is_vip and not self.date_vip:
            self.date_vip = datetime.now()
        await super().save(*args, **kwargs)


    @classmethod
    async def get_user(cls, id_telegram):
        return await cls.get_or_none(id_telegram=id_telegram)


    def __str__(self):
        return f'{self.username}'


