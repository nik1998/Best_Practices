import json
import requests
import urllib
for k in range(2,50):
    str = ""
    for i in range(0,k):
        str +='aaaaaaaaaaaaaaaa'
    url = 'http://82.148.16.44'
    port = '34764'
    url = url + ":"+port+"/encrypt"

    data = {
                'key': '7B83CEB6D3FCB70799234C73E5FD635D',
                'mode': 'ECB',
                'plaintext': str
            }
    headers = {'Content-type': 'application/json'}
    app_json = json.dumps(data)
    response = requests.post(url, data=app_json, headers=headers)
    json_response = response.json()
    json_response = json_response.get('result')
    print(json_response)

    ok = True
    str=""
    for i in range(64):
        str+=json_response[i-64]
        if json_response[i]!=json_response[i-64]:
            ok = False
            #break
    if ok:
        print(k)
        break