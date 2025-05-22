import requests

"""
https://example.com sahifasiga GET so'rov yuboring
va javob holatini (status_code) ekranga chiqaring.
"""
r=requests.get("https://example.com")
print(r.status_code)
