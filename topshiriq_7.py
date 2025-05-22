import requests

"""
https://jsonplaceholder.typicode.com/comments sahifasiga
`postId=1` parametrini yuboring va natijani ko'rsating.
"""
postId=78
r=requests.get(f"https://jsonplaceholder.typicode.com/comments?result={postId}")
data=r.json()
for i in data:
  print(i)
