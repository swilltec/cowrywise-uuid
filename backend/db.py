import logging


from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise, run_async

from config import DATABASE_URL, TESTING


logger = logging.getLogger(__name__)


async def init_db(app: FastAPI) -> None:
    DB_URL = "postgres://test:test@db-test:5432/test" \
        if TESTING else DATABASE_URL
    try:
        register_tortoise(
            app,
            db_url=DB_URL,
            modules={"models":  ["models"]},
            generate_schemas=True,
            add_exception_handlers=True,
        )

        logger.warning("--- DB CONNECTION WAS SUCCESSFUL ---")
    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR ---")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")
