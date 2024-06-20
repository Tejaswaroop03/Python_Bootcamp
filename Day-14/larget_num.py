s=input()
s1=input()
l=
for i in s:
    if i in '0123456789':
        l.append(int(i))
for i in s1:
    if i in '0123456789':
        l.append(int(i))
index=-1
low=10   
for i in range(0,len(l)):
    if l[i]%2==0:
        low=min(low,l[i])
        index=i
l.remove(low)
l.sort()
l.reverse()
l.append(low)
print(l)        




