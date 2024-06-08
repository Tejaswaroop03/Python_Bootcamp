l=list(map(int,input().split()))
x=[]
def rec(i,sum):
    if i>=len(l):   
          x.append(sum)
          return
    rec(i+2,sum+l[i])
    rec(i+1,sum)
rec(0,0)
print(x)
print(max(x))    
     

