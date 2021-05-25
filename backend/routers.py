import datetime
import uuid
from typing import List, Dict

from fastapi import Depends, APIRouter
from models import Keys



router = APIRouter()


@router.get("/")
async def home():
    await Keys.create(key=datetime.datetime.now(), uuid= uuid.uuid4().hex)
    keys = await Keys.all()
    return { i.key : i.uuid for i in keys}
