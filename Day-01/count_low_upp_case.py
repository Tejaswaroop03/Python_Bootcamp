l=input()
low_vow=up_vow=low_con=up_con=dig=spec=0

for i in l:
    if i.islower():
        if i in ['a','e','i','o','u']:
            low_vow+=1
        else:
            low_con+=1    
    elif i.isupper():
        if i in ['A','E','I','O','U']:
            up_vow+=1
        else:
            up_con+=1    
    elif i.isdigit():
        dig+=1
    else:
        spec+=1

print("lv-",low_vow)
print("uv-",up_vow)
print("lc-",low_con)
print("uc-",up_con)
print("dig-",dig)
print("spec-",spec)
    