m=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
a=int(input())
b=int(input())
n=len(m)
for i in range(n):
    for j in range(n):
        print(m[i][j],end=" ")
    print()    

def fun(i,j):
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
fun(a,b)
count=0
print()
for i in range(n):
    for j in range(n):
        print(m[i][j],end=" ")
        if m[i][j]==1:
            count+=1
    print()        
print(count)                                                