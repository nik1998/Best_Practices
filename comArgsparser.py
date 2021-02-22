import argparse
import requests


class Elem:
    count = 0
    key = ''
    minn = 10000000000
    maxx = -100000000000
    summ = 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=str)
    parser.add_argument('--not_mult', type=int, default=100)
    parser.add_argument('--smallest', type=int, default=0)
    args = parser.parse_args()
    dell = args.not_mult
    sm = args.smallest
    url = "http://" + args.host + ":" + args.port
    response = requests.get(url)
    json_response = response.json()
    res = {}
    keys =[]
    for el in json_response:
        for k in el:
            for v in el[k]:
                if v >= sm and v % dell != 0:
                    keys.append(k)
                    if k not in res:
                        res[k] = Elem()
                    res[k].count += 1
                    res[k].key = k
                    res[k].maxx = max(res[k].maxx, v)
                    res[k].minn = min(res[k].minn, v)
                    res[k].summ += v
    keys = list(set(sorted(keys)))
    f = open('truth.csv','w')
    for k in keys:
        st = ""
        st+=k+";"
        st += str(res[k].maxx) + ";"
        st += str(res[k].minn) + ";"
        st += str(float('{:.2f}'.format(res[k].summ/res[k].count))) + ";"
        st += str(res[k].summ) + "\n"
        f.write(st)
    f.close()