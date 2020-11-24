import base64
# st=""
# f = open("input.txt","r")
# for l in f.readlines():
#     st =st+l
#
# try:
#     while(True):
#         st =base64.b64decode(st).decode('utf-8') + '='
# except Exception:
#     f = open("output.txt","w")
#     f.write(st)



def xor(data, key):
    l = len(key)

    decoded = b""
    for i in range(0, len(data)):
        decoded += bytes([data[i] ^ key[i % l]])

    return decoded


f = open("input.txt","r")
num = [int(x) for x in f.readline().split()]
st =""
for d in num:
    r = (d //10 -1)*5 + (d+4)%5
    r+=ord('a')
    if r>ord('i'):
        r+=1
    st+=chr(r)
print(st)