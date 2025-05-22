import requests

"""
https://example.com sahifasiga GET so'rov yuboring
va javob matnini (text) konsolga chiqaring.
"""
r=requests.get('https://example.com')
print(r.text) 
