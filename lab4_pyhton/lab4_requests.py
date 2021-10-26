import requests

#GET Request
url = "https://api.tomorrow.io/v4/timelines"

querystring = {"units":"metric","timesteps":"1d","apikey":"iaUUFpAChKYe6EUIv6VbTgAduYAJIjSU", "location":"49.99977830463842, 36.249861874369856", "fields":"temperature"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

print("\nGET Request:")
print(response.text)

#POST Request
url = "https://ptsv2.com/t/lab4/post"

headers = {'content-type' : 'application/json'}

data = '{"title": "apple", "color": "red", "count": 23}'

response = requests.request("POST", url, params=data, headers=headers)

print("\nPOST Request:")
print(response.text)

#PUT Request
url = "https://reqbin.com/echo/put/json"

headers = {'content-type' : 'application/json'}

data = '{"Id": 123, "Customer": "John Smith", "Price": 10.00}'

response = requests.request("PUT", url, params=data, headers=headers) 

print("\nPUT Request:")
print(response.text)
