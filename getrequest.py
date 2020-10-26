import json
import requests
import urllib


url = input()
port = input()
a = input()
b = input()
url = url + ":"+port
response = requests.get(url , params={'a': a,'b': b})
json_response = response.json()
l = sorted(json_response,reverse=True)
for i in l:
    print(i)