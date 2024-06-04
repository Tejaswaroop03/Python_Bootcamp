n=int(input())
l=[]
for i in range(n):
    l.append(input())
st=input()
count=0
for i in st:
    if i in l[count]:
        count+=1
        if count%n==0:
            count=0
    else:
        print("no")
        exit()
print("yes")