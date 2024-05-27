from math import sqrt
n = int(input())
def prime(a):
    c=0
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            c+=1
            break
    return c

c = prime(n)
if c==0:
    print(n)
else:
    a = n+1
    while True:
        c = prime(a)
        if c==0:
            print(a,True)
            break
        a+=1