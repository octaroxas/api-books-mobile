from api.gateway.database import DatabaseAPI
from api.model.user import DBUser


class BooksUserController:
    def __init__(self) -> None:
        self.db = DatabaseAPI()

    def get_users(self) -> dict:
        user_table_data = self.db.get_data(table_name="users")
        user_db_dict = {}
        for user_data in user_table_data:
            username = user_data[-1]
            user_db_dict[username] = DBUser(
                name=user_data[1], email=user_data[2], hashed_password=user_data[3], nickname=user_data[4]
            ).dict()

        return user_db_dict

    def insert_user(self, user_data: DBUser) -> bool:
        return self.db.insert_data(table_name="users", data_dict=user_data.dict())
