'''n=input().split()
flo=even=odd=0
for i in n:
    if not i.isdecimal():
        flo+=float(i)
    else:
        i=int(i)
        if i%2==0:
            even+=int(i)
        else:
            odd+=int(i)        
print(flo,odd,even)   '''              

nums = input().split()
floats = 0
odd_sum = even_sum = 0
for num in nums:
    if "." in num:
        floats += float(num)
    else:
        num = int(num)
        if num%2:
            odd_sum+=num
        else:
            even_sum+=num
print(floats , odd_sum , even_sum)