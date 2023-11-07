import os
import sqlite3

conn = sqlite3.connect('c.db')
c = conn.cursor()

c.execute("CREATE TABLE if not exists users (id INTEGER, name TEXT, email TEXT, age INTEGER)")


def get_data() -> list[dict] | list:
    c.execute("SELECT id, name, email, age FROM users")
    users_data = c.fetchall()
    real_users = []

    for ud in users_data:
        real_users.append({
            'id': ud[0],
            'name': ud[1],
            'email': ud[2],
            'age': ud[3]
        })

    return real_users


# def get_option() -> int:
#     while True:
#         try:
#             option = int(input("Select an option: "))
#             return option
#         except ValueError:
#             print("Invalid option")


while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. Get users")
    print("2. Insert user")
    print("3. Update user")
    print("4. Delete user")
    print("X. Exit")
    # op: int = get_option()
    op = input("Select an option: ")

    match op:
        case "1":
            users = get_data()
            for user in users:
                print(f"({user['id']}) {user['name']}: {user['email']} - {user['age']}")
            input("Press enter to continue...")
        case "2":
            id_user = int(input("Enter id: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            c.execute(f"INSERT INTO users VALUES ({id_user}, '{name}', '{email}', {age})")
            conn.commit()
        case "3":
            id_user = int(input("Enter id: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            c.execute(f"UPDATE users SET name = '{name}', email = '{email}', age = {age} WHERE id = {id_user}")
            conn.commit()
        case "4":
            id_user = int(input("Enter id: "))
            c.execute(f"DELETE FROM users WHERE id = {id_user}")
            conn.commit()
        case _:
            break

conn.commit()
conn.close()
