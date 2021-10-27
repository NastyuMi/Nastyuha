import requests
import sqlite3

#GET Request
url_get = "https://api.tomorrow.io/v4/timelines"
querystring_get = {"units":"metric","timesteps":"1d","apikey":"iaUUFpAChKYe6EUIv6VbTgAduYAJIjSU", "location":"49.99977830463842, 36.249861874369856", "fields":"temperature"}
headers_get = {"Accept": "application/json"}
response_get = requests.request("GET", url_get, headers=headers_get, params=querystring_get)

print("\nGET Request:")
print(response_get.text)

#POST Requests
url_post = "https://ptsv2.com/t/lab4/post"
headers_post = {'content-type' : 'application/json'}
data_post = '{"title": "apple", "color": "red", "count": 23}'
response_post = requests.request("POST", url_post, params=data_post, headers=headers_post)

print("\nPOST Request:")
print(response_post.text)

#PUT Request
url_put = "https://reqbin.com/echo/put/json"
headers_put = {'content-type' : 'application/json'}
data_put = '{"Id": 123, "Customer": "John Smith", "Price": 10.00}'
response_put = requests.request("PUT", url_put, params=data_put, headers=headers_put) 

print("\nPUT Request:")
print(response_put.text)
try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite\n")

    cursor.execute("""DROP TABLE requests""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS requests(
        response TEXT);
        """)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""

    data_tuple = (response_get.text,)
    cursor.execute(sqlite_insert_with_param, data_tuple)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""

    data_tuple = (response_post.text,)
    cursor.execute(sqlite_insert_with_param, data_tuple)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""

    data_tuple = (response_put.text,)
    cursor.execute(sqlite_insert_with_param, data_tuple)

    cursor.execute("SELECT * FROM requests;")
    result = cursor.fetchmany(999)
    print(result)

    sqlite_connection.commit()
    print("\nЗапись успешно вставлена в таблицу requests ")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")