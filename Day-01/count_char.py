s=input()
i=count=1
while i< len(s):
    if s[i-1]==s[i]:
        count+=1
    else:
        print(s[i-1]+str(count),end="")
        count=1
    i+=1    
print(s[i-1]+str(count),end="")     
    

