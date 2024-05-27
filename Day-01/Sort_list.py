l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
i=j=0
while(i<len(l1) and i<len(l2)):
    if(l1[i]<l2[j]):
        print(l1[i],end=" ")
        i+=1
    else:
        print(l2[j],end=" ")
        j+=1
while(i<len(l1)):
    print(l1[i],end=" ")
    i+=1
while(j<len(l2)):
    print(l2[j],end=" ")
    j+=1

    