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
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        return True        
          
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

