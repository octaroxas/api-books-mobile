from typing import Union, Optional

from pydantic import BaseModel


class User(BaseModel):
    name: Optional[str] = None
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str
    expiration_time: None = None


class TokenData(BaseModel):
    username: Union[str, None] = None


class DBUser(User):
    password: str
    nickname: str


class CreatedUser(BaseModel):
    username: str
    status: str


class RemovedUser(CreatedUser):
    timestamp: float | None = None
