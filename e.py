from d import MyFetch

datas = MyFetch.get_data_db("c.db", "users")
for data in datas:
    print(data)


datas = MyFetch.get_data_api("https://jsonplaceholder.typicode.com/users")
for data in datas:
    print(data)
