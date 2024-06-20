n1=int(input())
n=str(n1)
if n==n[::-1]:
    print(n)
else:
    while(1):
        if n==n[::-1]:
            break
        n1+=1
        n=str(n1)
print(n)       

if len(n1)%2==0:
    temp=l[:len(n1)//2+1]
    

