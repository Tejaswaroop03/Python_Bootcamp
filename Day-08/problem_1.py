l=list(map(int,input().split()))
m=[]
c=0
while(c!=len(l)):
    r=[]
    for i in range(len(l)):
        if not str(l[i]).isalpha():
            if l[i] not in r:
                r.append(l[i])
                l[i]='a'
    m.append(r)
print(m)                







