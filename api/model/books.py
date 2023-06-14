from pydantic import BaseModel


class NewUserBook(BaseModel):
    title: str
    author: str
    pages: int
    isbn: str | None = None
    user_id: int


class StdUserBook(BaseModel):
    book_id: int
    title: str
    author: str
    pages: int
    isbn: str | None = None
    created_at: str
    favorited: bool = False


class UserBook(StdUserBook):
    user_id: int


class RemovedBook(BaseModel):
    user: int
    title: str
    status: str
