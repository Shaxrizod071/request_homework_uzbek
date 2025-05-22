import requests

"""
3-topshiriqdagi JSON javobdan "title" maydonini
ajratib olib konsolga chiqaring.
"""
param={'title': 'delectus aut autem'}
url=('https://jsonplaceholder.typicode.com/todos/1')
r=requests.get(url,params=param)
print(r.url)
