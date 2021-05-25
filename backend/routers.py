import datetime
import uuid
from typing import List

from fastapi import Depends, APIRouter
from models import Keys, Keys_Pydantic



router = APIRouter()


@router.get("/", response_model=dict)
async def home():
    await Keys.create(key=datetime.datetime.now(), uuid= uuid.uuid4().hex)
    keys = await Keys.all()
    return { i.key : i.uuid for i in keys}
