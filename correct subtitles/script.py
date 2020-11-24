

f = open("l1.txt","r")
st=""
pr=0
for i in f.readlines():
    i = i.replace("\n","")
    if len(i)>1:
        if pr==0:
            st+=i
        else:
            st = st +" " + i
    d = len(i.split())
    pr+=d
    if pr>10:
        st+="\n"
        pr=0


f = open("l1out.txt","w")
f.write(st)