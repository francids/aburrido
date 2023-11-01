import sqlite3

conn = sqlite3.connect('c.db')
c = conn.cursor()

# c.execute("DELETE FROM users")
# c.execute("DROP TABLE users")

# # Create table
# c.execute("CREATE TABLE users (id INTEGER, name TEXT, email TEXT, age INTEGER)")
# c.execute("INSERT INTO users VALUES (1, 'Francisco Mesa', 'fmesa@mail.com', 20)")
# c.execute("INSERT INTO users VALUES (2, 'Angel Castillo', 'acastillo@mail.com', 25)")
# c.execute("INSERT INTO users VALUES (3, 'Carla Espinal', 'cespinal@mail.com', 23)")
# c.execute("INSERT INTO users VALUES (4, 'Jose Perez', 'jperez@mail.com', 30)")
# c.execute("INSERT INTO users VALUES (5, 'Maria Lopez', 'mlopez@mail.com', 28)")
# c.execute("INSERT INTO users VALUES (6, 'Juan Hernandez', 'jhernandez@mail.com', 35)")
# c.execute("INSERT INTO users VALUES (7, 'Pedro Sanchez', 'psanchez@mail.com', 40)")

# Get data from table
c.execute("SELECT id, name, email, age FROM users ORDER BY age ASC")
users = c.fetchall()
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
