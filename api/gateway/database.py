import psycopg2

from typing import List
from psycopg2.extensions import cursor


class DatabaseAPI:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            database="books_mobile",
            host="lr-netserver.blue-stonecat.ts.net",
            user="books",
            password="books",
            port="5432"
        )
        self.database: cursor = self.conn.cursor()

    def make_query(self, query_stmt: str) -> List[tuple]:
        self.database.execute(query=query_stmt)

        query_data = self.database.fetchall()
        return query_data
