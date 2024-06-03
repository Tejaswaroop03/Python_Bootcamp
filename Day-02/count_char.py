string=input()
count=0
for i in string:
    if i=='f':
        count+=1
    elif i=='m':
        count-=1
if count==0:
    print(0)
elif count>0:
    print('f')
else:
    print('m')                    