from d import MyFetch

datas_db = MyFetch.get_data_db("database/1.db", "users")
for row in datas_db:
    print(row)

datas_api = MyFetch.get_data_api("https://jsonplaceholder.typicode.com/users")
for data in datas_api:
    print(data)
