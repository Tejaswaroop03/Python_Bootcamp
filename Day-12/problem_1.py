l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
sum=0
l=[]
def re1(b,c):
    if c==len(l2):
        return 
    if(l2[c]%2!=0):
        l.append(l1[b]+l2[c])
    re1(b,c+1)    
def re(i):
    j=0
    if i==len(l1):
        return 
    if l1[i]%2==0:
        re1(i,j)
    re(i+1)

re(0)
print(l)


    
    