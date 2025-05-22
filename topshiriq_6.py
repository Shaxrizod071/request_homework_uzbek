import requests

"""
5-topshiriqdagi ro'yxat nechta foydalanuvchidan
iborat ekanligini hisoblang va konsolga chiqaring.
"""
r=requests.get('https://jsonplaceholder.typicode.com/users')
data=r.json()
for i in data:
   print(len(i))
