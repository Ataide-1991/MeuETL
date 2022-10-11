from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class UserEstado(BaseModel):
    uid:str
    uf:str
    state:str
    cases:str
    deaths:str
    suspects:str
    refuses:str
    datetime:str


