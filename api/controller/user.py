from typing import List

from api.gateway.database import DatabaseAPI


class BooksUserController:
    def __init__(self) -> None:
        self.db = DatabaseAPI()
        self.users = self.db.get_users()

    def get_users(self) -> List[tuple]:
        return self.users
