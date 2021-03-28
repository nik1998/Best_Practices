import json
import requests
import time
import threading
import random
import math

payload = {}
ans = []
dmin = 0.0
dx = 0
dy = 0

lock = threading.Lock()


def sendFinal(x, y):
    for i in range(3):
        url = "https://battleship.q.2021.ugractf.ru/c81887052bd46efa/fire"
        response = requests.post(url, data={'x': int(x), 'y': int(y)}, cookies=payload)
        json_response = response.json()
        print(json_response)


def sendRequest():
    global dx, dy, dmin
    for i in range(3):
        url = "https://battleship.q.2021.ugractf.ru/c81887052bd46efa/fire"
        lock.acquire()
        x = random.randrange(-int(dmin), int(dmin) + 1)
        r = int(math.sqrt(dmin * dmin - x * x))
        y = dy + random.randrange(-r, r + 1)
        x += dx
        if dmin <= 2.0 and dmin != 0.0:
            threading.Thread(target=sendFinal, args=(dx - 1, dy - 1)).start()
            threading.Thread(target=sendFinal, args=(dx - 1, dy)).start()
            threading.Thread(target=sendFinal, args=(dx - 1, dy + 1)).start()
            threading.Thread(target=sendFinal, args=(dx, dy - 1)).start()
            threading.Thread(target=sendFinal, args=(dx, dy)).start()
            threading.Thread(target=sendFinal, args=(dx, dy + 1)).start()
            threading.Thread(target=sendFinal, args=(dx + 1, dy - 1)).start()
            threading.Thread(target=sendFinal, args=(dx + 1, dy)).start()
            threading.Thread(target=sendFinal, args=(dx + 1, dy + 1)).start()
        lock.release()
        response = requests.post(url, data={'x': int(x), 'y': int(y)}, cookies=payload)
        json_response = response.json()
        d = float(json_response['distance'])
        lock.acquire()
        if dmin == 0:
            dmin = d
        elif d < dmin:
            dx = x
            dy = y
            dmin = d
            print(dmin)
            if dmin <= 1:
                print(json_response)
                print('Interesting')
        lock.release()
        # print(json_response)



while True:
    with requests.Session() as session:

        initial_response = session.post("https://battleship.q.2021.ugractf.ru/c81887052bd46efa/reset")
        s = session.cookies
        payload['AIOHTTP_SESSION'] = session.cookies['AIOHTTP_SESSION']
        for i in range(50):
            threading.Thread(target=sendRequest).start()

        # url = "https://battleship.q.2021.ugractf.ru/c81887052bd46efa/reset"
        # response = requests.post(url, data=payload)
        # json_response = response.json()
        # print(json_response)
        time.sleep(3)
        if dmin == 0:
            print('Interesting')
            exit(-1)
        dmin = 0.0
        dx = 0
        dy = 0
