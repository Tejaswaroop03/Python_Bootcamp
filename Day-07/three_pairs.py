def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
            print("curr:",curr,"curr+[l[i]]:",curr+[l[i]],"i+1:",i+1)
    fun([],0)    


l=list(map(int,input().split()))
k=int(input())
''''for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            count+=1
            print((l[i],l[j],l[k]))'''
combination(l,k)





