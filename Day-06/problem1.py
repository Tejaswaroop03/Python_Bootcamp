from collections import defaultdict
l=list(map(int,input().split()))
def val():
    return 0
d=defaultdict(val)
for i in range(len(l)):
    d[i]+=1
for i in d:
    if(d[i]>len(l)//2):
        print(i)

