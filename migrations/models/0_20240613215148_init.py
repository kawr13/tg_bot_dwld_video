from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(255),
    "first_name" VARCHAR(255),
    "last_name" VARCHAR(255),
    "phone" VARCHAR(255),
    "email" VARCHAR(255),
    "id_telegram" VARCHAR(255) NOT NULL,
    "is_vip" INT,
    "date_vip" TIMESTAMP,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
