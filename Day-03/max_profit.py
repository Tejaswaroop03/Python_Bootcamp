l=list(map(int,input().split()))
profit=0
buy=l[0]
for i in range(1,len(l)):
    if l[i]<buy:
        buy=l[i]
    elif l[i]-buy>profit:
        profit=l[i]-buy
print(profit)        

    