from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

app: Flask = Flask(__name__)


def get_data_db_table(db: str, table: str) -> list | None:
    data: list | None = None
    try:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {table}")
        data: list = c.fetchall()
        conn.close()
    except Exception as e:
        print("Error: ", e)
    return data


@app.route('/')
def index():
    users: list | None = get_data_db_table(os.getenv("DATABASE_URL"), 'users')
    if users is None:
        return jsonify({'error': 'Error in database'})
    else:
        real_users: list = []

        for user in users:
            real_users.append({
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'age': user[3]
            })

        return jsonify(real_users)


if __name__ == '__main__':
    app.run()
