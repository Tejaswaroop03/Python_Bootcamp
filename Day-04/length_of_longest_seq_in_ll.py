class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
class sll:
    def __init__(self):
        self.head=None
        
    def add_back(self,x):
        temp=node(x)
        if self.head==None:
            self.head=temp
        else:
            t=self.head
            while(t.nxt!=None):
                t=t.nxt
            t.nxt=temp
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"->",end="")
            temp=temp.nxt

    def longest_sub_seq(self):
        temp=self.head
        l=0
        count=1
        while temp.nxt!=None:
            if temp.data+1==temp.nxt.data:
                count+=1
            else:
                l=max(l,count)
                count=1
            temp=temp.nxt
        l=max(l,count)    
        print(l)        

l1=sll()
l1.add_back(1)
l1.add_back(2)
l1.add_back(3)
l1.add_back(4)
l1.add_back(7)
l1.add_back(8)
l1.add_back(9)
l1.add_back(3)
l1.display()
print()
l1.longest_sub_seq()


