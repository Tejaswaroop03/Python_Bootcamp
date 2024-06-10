from collections import Counter
s=input()
count=0
for i in s:
    if i.islower():
        count+=1
if count==26:
    print("yes")
else:
    print("no")            
