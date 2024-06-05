n=int(input())
for i in range(2*n-1):
    for j in range(2*n-1):
        print(min(min(j+1,(2*n)-j-1),min(i+1,(2*n)-i-1)),end=" ")
    print()    
