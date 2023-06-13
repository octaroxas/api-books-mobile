import os
from typing import List, Tuple

import psycopg2
from dotenv import load_dotenv
from loguru import logger
from psycopg2 import OperationalError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extensions import cursor


class DatabaseAPI:
    def __init__(self) -> None:
        self.conn, self.database = self.__db_startup()

    @staticmethod
    def __load_db_env(meta_key: str) -> str | None:
        env_file = f"{os.getcwd()}/env/.env"
        env_loaded = load_dotenv(dotenv_path=env_file)
        env_mode = str(os.getenv("ENVIRONMENT"))
        if env_loaded:
            env_db_data = {
                "db_name": str(os.getenv("DB_NAME")),
                "db_usr": str(os.getenv("DB_USR")),
                "db_pwd": str(os.getenv("DB_PWD")),
                "db_port": str(os.getenv("DB_PORT")),
                "db_host": str(os.getenv("DB_HOST")) if env_mode == "dev" else "localhost",
            }
            return env_db_data.get(meta_key, None)
        else:
            raise EnvironmentError("Error loading .env file. Check your project files.")

    def __db_startup(self) -> Tuple[None, cursor]:
        try:
            db_cx = psycopg2.connect(
                database=self.__load_db_env(meta_key="db_name"),
                host=self.__load_db_env(meta_key="db_host"),
                user=self.__load_db_env(meta_key="db_usr"),
                password=self.__load_db_env(meta_key="db_pwd"),
                port=self.__load_db_env(meta_key="db_port"),
            )
            db_cur = db_cx.cursor()
        except OperationalError:
            db_cx, db_cur = self.__initialize_db()

        return db_cx, db_cur

    def __initialize_db(self) -> Tuple[None, cursor]:
        init_cx = psycopg2.connect(
            database="postgres",
            host=self.__load_db_env(meta_key="db_host"),
            user=self.__load_db_env(meta_key="db_usr"),
            password=self.__load_db_env(meta_key="db_pwd"),
            port=self.__load_db_env(meta_key="db_port")
        )
        init_cursor = init_cx.cursor()
        init_cx.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with open("/code/database/scripts/initialize_db.sql", "r") as init_script:
            sql_init = init_script.readlines()

        init_cmds = []
        sql_cmd = ""
        for cmd in sql_init:
            sql_cmd += cmd
            if ";" in cmd:
                init_cmds.append(sql_cmd.strip().replace("\n", ""))
                sql_cmd = ""
                continue

        init_stmt = (
            "CREATE DATABASE books_mobile;"
        )
        init_cursor.execute(query=init_stmt)

        init_cx = psycopg2.connect(
            database="books_mobile",
            host=self.__load_db_env(meta_key="db_host"),
            user=self.__load_db_env(meta_key="db_usr"),
            password=self.__load_db_env(meta_key="db_pwd"),
            port=self.__load_db_env(meta_key="db_port")
        )
        init_cursor = init_cx.cursor()
        for cmd in init_cmds:
            logger.debug(cmd)
            init_cursor.execute(query=cmd)
            init_cx.commit()

        return init_cx, init_cursor

    def make_query(self, query_stmt: str) -> List[tuple]:
        self.database.execute(query=query_stmt)

        query_data = self.database.fetchall()
        return query_data

    def get_data(self, table_name: str, filters: dict | None = None, filter_by_all: bool = False) -> List[tuple]:
        query_stmt = f"SELECT * FROM {table_name}"
        conditional_stmt = "AND" if filter_by_all else "OR"

        if filters is not None:
            query_stmt += " WHERE "
            for _filter in filters.keys():
                query_stmt += f"{_filter} {filters[_filter]}"
                if len(filters.keys()) > 1:
                    query_stmt += f" {conditional_stmt} "
        query_stmt += ";"
        query_stmt = query_stmt.strip()

        print(query_stmt)
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
            self.conn.commit()
            return True
        except Exception as insert_err:
            logger.error(f"Error inserting new data into {table_name} table. Error/Exception: {insert_err}.")
            return False

    def remove_data(self, sql_query: str) -> int:
        print(sql_query)
        try:
            self.database.execute(query=sql_query)
            lines_affected = self.conn.commit()
            return lines_affected
        except Exception as rm_err:
            logger.error(f"Error executing the removal SQL Query. Error/Exception: {rm_err}.")
            return False

