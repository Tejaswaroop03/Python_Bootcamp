s=input()
l=0
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp+=s[j]
        else:
            l=max(l,len(temp))
            break
print(l)

'''i=j=0
le=0
while(j!=len(s)-1):
    j=i+1
    temp=s[i]
    while(j!=len(s)):
        if s[j] not in temp:
            temp+=s[j]
            j+=1
        else:
            le=max(le,len(temp))
            i=i+1
            break
print(le)'''        
                




        

