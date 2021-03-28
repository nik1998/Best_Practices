import requests
import time
import re

i = 8000
im=-1
minn = 1000
while i < 10000:
    url = "https://oeis.org/search?q=signed: " + str(i) + "%2C&sort=number&language=&go=Search"
    response = requests.get(url)
    txt = response.text
    regex_num = re.compile('\d+\sresults')
    s = regex_num.search(txt)
    print("Iteration: " + str(i))
    ans = int(txt[s.start():s.end() - 8])
    print('count:' + str(ans))
    if minn > ans:
        minn =ans
        im = i
    if ans <= 5:
        print("Result: " + str(i))
    i += 1
print(minn)
print(im)