class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                t.d[i]=node()
            t=t.d[i]
        t.flag=1 

    def search(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:                    
            return False                      
    def search_prefix(self,str):
        l=[]
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i] 
        return True
    
    def all_prefix(self,str):
        def fun(t,s):
            if (t.flag==1):
                print(s)
                return 
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s="" 
        for i in str:
            if(i in t.d):
                t=t.d[i]
        fun(t,s)        

    def bfs(self):
        t=self.root
        if flag==1:
            print(t.d)
        bfs(t.d[i])



          
t1=tries()        
'''t1.insert('world')
t1.insert('wood')
t1.insert('worst')
print(t1.search('wood'))
print(t1.search_prefix('wor'))'''
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search(s))
    if(a=='3'):
        print(t1.search_prefix(s))        

