l=list(map(int,input().split()))
def st(a,b,c):
    s=a+b+c
    p=min(a,b,c)
    q=max(a,b,c)
    r=s-p-q
    l[i]=p
    l[i+1]=q
    l[i+2]=r
for i in range(len(l)-2):
    st(l[i],l[i+1],l[i+2])
print(l)    



