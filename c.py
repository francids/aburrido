import sqlite3
from sqlite3 import Cursor

conn = sqlite3.connect('database/1.db')
db_cursor: Cursor = conn.cursor()

# db_cursor.execute("DELETE FROM users")
# db_cursor.execute("DROP TABLE users")

# # Create table
# db_cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, email TEXT, age INTEGER)")
# db_cursor.execute("INSERT INTO users VALUES (1, 'Francisco Mesa', 'fmesa@mail.com', 20)")
# db_cursor.execute("INSERT INTO users VALUES (2, 'Angel Castillo', 'acastillo@mail.com', 25)")
# db_cursor.execute("INSERT INTO users VALUES (3, 'Carla Espinal', 'cespinal@mail.com', 23)")
# db_cursor.execute("INSERT INTO users VALUES (4, 'Jose Perez', 'jperez@mail.com', 30)")
# db_cursor.execute("INSERT INTO users VALUES (5, 'Maria Lopez', 'mlopez@mail.com', 28)")
# db_cursor.execute("INSERT INTO users VALUES (6, 'Juan Hernandez', 'jhernandez@mail.com', 35)")
# db_cursor.execute("INSERT INTO users VALUES (7, 'Pedro Sanchez', 'psanchez@mail.com', 40)")

# Get data from table
db_cursor.execute("SELECT id, name, email, age FROM users ORDER BY age ASC")
users = db_cursor.fetchall()
real_users = []

for user in users:
    real_users.append({
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'age': user[3]
    })

for user in real_users:
    print(f"({user['id']}) {user['name']}: {user['email']} - {user['age']}")

conn.commit()
conn.close()
