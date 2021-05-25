from starlette.config import Config
from starlette.datastructures import Secret

from databases import DatabaseURL

config = Config(".env")

PROJECT_NAME = "Cowrywise demo uuid project"
VERSION = "1.0.0"
API_PREFIX = ""

TESTING = config("TESTING", cast=bool, default=False)

POSTGRES_USER = config("POSTGRES_USER", cast=str, default="postgres")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default="postgres")
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str, default="postgres")

DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa