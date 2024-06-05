n=int(input())
ascii=97
for i in range(n):
    for j in range(n-i):
        print("-",end=" ")
    for k in range(2*i+1):
        print(chr(ascii),end=" ")
        ascii+=1
    for l in range(n-i):
        print("-",end=" ")
    ascii=97    
    print()
       

