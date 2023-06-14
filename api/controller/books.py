from typing import List
from datetime import datetime

from api.gateway.database import DatabaseGateway
from api.model.books import UserBook, StdUserBook, NewUserBook


class BooksController:
    def __init__(self) -> None:
        self.data_src = "books"
        self.db = DatabaseGateway()

    def get_user_books(self, user_id: int) -> List[dict]:
        user_filter = {"users_id": user_id}
        books_table_data = self.db.get_data(table_name="books", filters=user_filter, filter_by_all=True)
        books_db_dict = []
        for book_info in books_table_data:
            conv_timestamp = datetime.fromtimestamp(book_info[5])
            book_data = StdUserBook(
                book_id=book_info[0], title=book_info[1], author=book_info[2], pages=book_info[3], isbn=book_info[4],
                created_at=conv_timestamp, favorited=book_info[6]
            ).dict()
            books_db_dict.append(book_data)

        return books_db_dict

    def insert_book(self, book_data: NewUserBook) -> bool:
        return self.db.insert_data(table_name="books", data_dict=book_data.dict())

    def delete_book(self, book_data: UserBook) -> dict:
        book_id = book_data.book_id
        book_title = book_data.title
        user_id = book_data.user_id
        query = (
            f"DELETE FROM books WHERE books.id = {book_id} AND books.user_id = {user_id};"
        )
        removed_data = self.db.remove_data(sql_query=query)

        if removed_data != 0:
            return {"user": user_id, "title": book_title, "status": "removed"}
        else:
            return {"user": user_id, "title": book_title, "status": "failed"}
