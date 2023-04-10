import os
from typing import List, Optional

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import cursor


class DatabaseAPI:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            database=self.__load_db_env(meta_key="db_name"),
            host=self.__load_db_env(meta_key="db_host"),
            user=self.__load_db_env(meta_key="db_usr"),
            password=self.__load_db_env(meta_key="db_pwd"),
            port=self.__load_db_env(meta_key="db_port")
        )
        self.database: cursor = self.conn.cursor()

    @staticmethod
    def __load_db_env(meta_key: str) -> Optional[str]:
        env_file = f"{os.getcwd()}/env/.env"
        env_loaded = load_dotenv(dotenv_path=env_file)
        if env_loaded:
            env_db_data = {
                "db_name": str(os.getenv("DB_NAME")),
                "db_usr": str(os.getenv("DB_USR")),
                "db_pwd": str(os.getenv("DB_PWD")),
                "db_port": str(os.getenv("DB_PORT")),
                "db_host": str(os.getenv("DB_HOST")),
            }
            return env_db_data.get(meta_key, None)
        else:
            raise EnvironmentError("Error loading .env file. Check your project files.")

    def make_query(self, query_stmt: str) -> List[tuple]:
        self.database.execute(query=query_stmt)

        query_data = self.database.fetchall()
        return query_data

    def get_users(self) -> List[tuple]:
        query_stmt = "SELECT * FROM users;"

        users_list = self.make_query(query_stmt=query_stmt)
        return users_list
