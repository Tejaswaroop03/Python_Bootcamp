s=input()
n=int(input())
l=len(s)
s1=[]
for i in range(n):
    c,n1=input().split()
    if c=='L':
        c=s[int(n1)%l]
        s1+=[c]
    else:
        c=s[-1*(int(n1)%l)]
        s1+=[c]        
print(s1)        
s1.sort()
s1 ="".join(s1) 
print(s1)          
i=0
flag=1
temp=[]
while(i!=len(s)): 
    if len(temp)==len(s1):
        print(temp)
        temp.sort()
        temp = "".join(temp)
        if temp==s1:
            flag=0
            print("yes")
            break
        else:
            temp=[]
            i-=n-1    
    temp+=s[i]
    i+=1    
if flag:
    print("no")   

  






