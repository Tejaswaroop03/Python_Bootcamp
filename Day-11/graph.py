def min_cost(d,x,e,c,m,l1):
    l.append(x)
    if(x==e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=min_cost(d,i[0],e,c+i,m,l1)
    l.pop()
    return m,l1


            
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

#d={5:[7,3],3:[5,7,8],7:[5,3,4],4:[7,8,2],8:[4,3,2],2:[4,8]}
d = {5:[(7,1),(3,2)],7:[(5,1),(4,5),(3,3)],4:[(7,5),(8,2),(2,2)],8:[(3,2),(4,2),(2,3)],3:[(5,2),(7,3),(8,2)],2:[(4,2),(8,3)]}
l=[]
#fun(d,5)
print(l)
all(d,5)
min_cost(d,5,2,0,9999999,[])