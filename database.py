from contextlib import asynccontextmanager

from tortoise import Tortoise


TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["models.users", "aerich.models"],
            "default_connection": "default",
        },
    },
}


@asynccontextmanager
async def init():
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()
        yield
    finally:
        await Tortoise.close_connections()


async def init_not_manager():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def destroy():
    await Tortoise.close_connections()
