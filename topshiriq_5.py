import requests

"""
https://jsonplaceholder.typicode.com/users manzilidan
foydalanuvchilar ro'yxatini oling va
ularning ismlarini chiqarib bering.
"""
r=requests.get('https://jsonplaceholder.typicode.com/users')
data=r.json()
print(data)
