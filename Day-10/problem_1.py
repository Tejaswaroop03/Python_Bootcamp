'''Question:You have given an array in increasing order where all the elements are non-prime numbers,find sum of all the largest prime numbers bewteen arr[0]&arr[1],arr[1]&arr[2]......'''
from math import sqrt
l=list(map(int,input().split()))
def prm(a,b):
    mx=0
    for i in range(b-1,a,-1):
        f=True
        for j in range(2,int(sqrt(i))+1):
            if(i%j==0):
                f=False
                break
        if f:
            mx=max(mx,i)
            break  
    return mx
s=0        
for i in range(len(l)-1):
    s+=prm(l[i],l[i+1])
print(s)        

