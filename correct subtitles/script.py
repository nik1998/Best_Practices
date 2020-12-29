f = open("program", "r")
st = ""
ar = [0] * 1000000
pr = 0
mx = 0
ans=""
v = []
cl = []
p =0
st1=''
for l in f.readlines():
    d = 0
    oct = ''
    l = l.replace('[-]', 'z')
    for i in l:
        if i == '+':
            d += 1
        else:
            if i == '-':
                d -= 1
            else:
                if d == 0:
                    oct = l
                    break
                oct += i
    ar[pr] += d
    if d!=0:
        st1+=str(d)
        if ar[pr]<128:
            if pr!=p and pr != p+1:
                st+="\n"
            p=pr
            st += chr(ar[pr])
    if l != "\n":
        st1+=oct
        for i in oct:
            if i == '>':
                pr += 1
            elif i == '<':
                pr -= 1
            elif i == '.':
                ans += chr(ar[pr])
            elif i == 'z':
                if pr in v:
                    cl.append(pr)
                ar[pr] = 0
            elif i == ',':
                v.append(pr)
    mx = max(mx, pr)
f = open("out.txt", "w")
print(str(v))
print(str(cl))
ff=[]
d={}
for i in ar:
    if i>256:
        ff.append(i)
        d[i]=1
ff = sorted(ff)

print(len(d))
print(len(ff))
f.write(st)
f.close()
f = open("out3.txt", "w")
f.write(st1)