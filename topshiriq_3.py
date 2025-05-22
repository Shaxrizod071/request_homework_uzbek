import requests

"""
https://jsonplaceholder.typicode.com/todos/1 sahifasiga so'rov yuboring
va JSON javobini chiqarib bering.
"""
r=requests.get('https://jsonplaceholder.typicode.com/todos/1')
data=r.json()
print(data)
