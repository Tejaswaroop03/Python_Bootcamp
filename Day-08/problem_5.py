m=[['t','u','e','d'],['f','w','o','w'],['r','o','e','r'],['d','r','u','i']]
s=input()
n=len(m)
for i in range(n):
    for j in range(n):
        print(m[i][j],end=" ")
    print()    

def fun(i,j,k,t):
    if m[i][j]==0:
        return
    else:
        m[i][j]=0

    if i>0:
        fun(i-1,j)
    if i<n-1:
        fun(i+1,j)
    if j>0:
        fun(i,j-1)
    if j<n-1:
        fun(i,j+1)
for i in range(n):
    for j in range(n):
        print(m[i][j],end=" ")
        if m[i][j]==1:
            count+=1
    print()        
print(count)                                                