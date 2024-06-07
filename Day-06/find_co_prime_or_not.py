from math import sqrt
n1=int(input())
n2=int(input())
flag=0
for i in range(2,int(sqrt(min(n1,n2))+1)):
               if(n1%i==0 and n2%i==0):
                       flag=1
                       break
if flag==1:
        print("not a coprime")
else:
        print("co-primes")        

               
               