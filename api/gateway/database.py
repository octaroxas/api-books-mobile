import os
from typing import Optional, List

import psycopg2
from loguru import logger
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

    def get_data(self, table_name: str) -> List[tuple]:
        query_stmt = f"SELECT * FROM {table_name};"

        db_data = self.make_query(query_stmt=query_stmt)
        return db_data

    def insert_data(self, table_name: str, data_dict: dict) -> bool:
        query_stmt = f"INSERT INTO {table_name} VALUES (DEFAULT, "
        for field in data_dict.keys():
            query_stmt += f"'{data_dict[field]}', "

        query_stmt = query_stmt[:-2]
        query_stmt += ");"
        print(query_stmt)
        try:
            self.database.execute(query=query_stmt)
            return True
        except Exception as insert_err:
            logger.error(f"Error inserting new data into {table_name} table. Error/Exception: {insert_err}.")
            return False
