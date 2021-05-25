from pydantic import BaseModel
from datetime import datetime

class Keys(BaseModel): 
    key: datetime
    uuid: str