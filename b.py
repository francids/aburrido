import requests
import json


def get_data(url: str):
    try:
        data = json.loads(requests.get(url).text)
    except Exception as e:
        print(e)
        data = None
    return data


def main():
    users = get_data("https://jsonplaceholder.typicode.com/users")
    for user in users:
        print(f"({user['id']}) {user['name']}: {user['email']}")


if __name__ == "__main__":
    main()
