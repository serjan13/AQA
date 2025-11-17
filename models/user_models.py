from pydantic import BaseModel
from typing import List

class Users(BaseModel):
    avatar_url: str
    email: str
    name: str
    nickname: str
    uuid: str

class Meta(BaseModel):
    total: int

class UsersResponse(BaseModel):
    meta: Meta
    users: List[Users]