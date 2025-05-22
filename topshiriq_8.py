import requests

"""
https://jsonplaceholder.typicode.com/posts manziliga
quyidagi ma'lumotlarni POST qilib yuboring:
{
    "title": "Mening sarlavham",
    "body": "Bu mening birinchi postim.",
    "userId": 1
}
Va javobdagi JSONni ko'rsating.
"""
dct={
    "title": "Mening sarlavham",
    "body": "Bu mening birinchi postim.",
    "userId": 1
}
r=requests.post('https://jsonplaceholder.typicode.com/posts', json=dct)
print(list(r))
