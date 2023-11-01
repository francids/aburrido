import sqlite3

conn = sqlite3.connect('c.db')
c = conn.cursor()

c.execute("CREATE TABLE if not exists users (id INTEGER, name TEXT, email TEXT, age INTEGER)")


def get_data():
    c.execute("SELECT id, name, email, age FROM users")
    users = c.fetchall()
    real_users = []

    for user in users:
        real_users.append({
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'age': user[3]
        })

    return real_users


def insert_data(id_user: int, name: str, email: str, age: int):
    c.execute(f"INSERT INTO users VALUES ({id_user}, '{name}', '{email}', {age})")
    conn.commit()


def update_data(id_user: int, name: str, email: str, age: int):
    c.execute(f"UPDATE users SET name = '{name}', email = '{email}', age = {age} WHERE id = {id_user}")
    conn.commit()


def delete_data(id_user: int):
    c.execute(f"DELETE FROM users WHERE id = {id_user}")
    conn.commit()


while True:
    print("1. Get data")
    print("2. Insert data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Exit")
    option = int(input("Select an option: "))

    if option == 1:
        users = get_data()
        for user in users:
            print(f"({user['id']}) {user['name']}: {user['email']} - {user['age']}")
    elif option == 2:
        id_user = int(input("Enter id: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        insert_data(id_user, name, email, age)
    elif option == 3:
        id_user = int(input("Enter id: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        update_data(id_user, name, email, age)
    elif option == 4:
        id_user = int(input("Enter id: "))
        delete_data(id_user)
    elif option == 5:
        break
    else:
        print("Invalid option")

conn.commit()
conn.close()
