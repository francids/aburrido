from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


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


@app.route('/')
def index():
    users = get_data_db('c.db', 'users')
    if users is None:
        return jsonify({'error': 'Error in database'})
    else:
        real_users = []

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
