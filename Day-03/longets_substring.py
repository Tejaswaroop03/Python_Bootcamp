st=input()
i=l=0
j=count=1
while j<len(st):
    if (ord(st[i]))+1==ord(st[j]):
        count+=1
        i+=1
        j+=1
    else:
        l=max(l,count)
        count=1
        i+=1
        j+=1
print(l)

"""st=input()
i=0
j=0
l=0
while j<len(st)-1:
    if ord(st[j])+1==ord(st[j+1]):
        j+=1
    else:
        j+=1
        l=max(l,j-i)
        i=j

print(l)"""         
