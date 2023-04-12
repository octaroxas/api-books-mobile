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
    hashed_password: str
    nickname: str
