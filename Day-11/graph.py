def fun(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            fun(d,i)

def all(a,x):
    l.append(x)
    if(x==2):
        print(l)
        l.pop()
        return
    for i in a[x]:
        if i not in l:
            all(a,i)
    l.pop()                    

d={5:[7,3],3:[5,7,8],7:[5,3,4],4:[7,8,2],8:[4,3,2],2:[4,8]}
l=[]
#fun(d,5)
print(l)
all(d,5)