from typing import List

from api.gateway.database import DatabaseAPI
from api.model.user import NewUser


class BooksUserController:
    def __init__(self) -> None:
        self.db = DatabaseAPI()

    def get_users(self) -> List[tuple]:
        return self.db.get_data(table_name="users")

    def insert_user(self, user_data: NewUser) -> bool:
        return self.db.insert_data(table_name="users", data_dict=user_data.dict())
