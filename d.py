import requests
import json
import sqlite3


class MyFetch:
    @staticmethod
    def get_data_api(api: str):
        try:
            data = json.loads(requests.get(api).text)
        except Exception as e:
            print(e)
            data = None
        return data

    @staticmethod
    def get_data_db(db: str, table: str):
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            c.execute(f"SELECT * FROM {table}")
            data = c.fetchall()
            conn.close()
        except Exception as e:
            print(e)
            data = None
        return data

    @staticmethod
    def get_data_db_where(db: str, table: str, where: str):
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            c.execute(f"SELECT * FROM {table} WHERE {where}")
            data = c.fetchall()
            conn.close()
        except Exception as e:
            print(e)
            data = None
        return data
