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

    def add_front(self,x):
        temp=node(x)
        if self.head==None:
            self.head=temp
        else:
            temp.nxt=self.head
            self.head=temp

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"->",end="")
            temp=temp.nxt

    def search(self,x):
        if self.head==None:
            print("ll is empty")
        temp=self.head
        while temp!=None:
            if temp.data==x:
                print("yes",temp.data,"is present in ll")
                break
            else:
                temp=temp.nxt
        if temp==None:
            print("not found in ll")

    def remove_front(self):
        temp=self.head
        temp1=temp.nxt
        self.head=temp1

    def remove_back(self):
        temp=self.head
        while temp.nxt.nxt!=None:
            temp=temp.nxt
        temp.nxt=None    



    def middle_node(self):
        fast=slow=self.head
        while(fast!=None and fast.nxt!=None):
            fast=fast.nxt.nxt
            slow=slow.nxt
        print("middle node:",slow.data)
        if(fast==None):
            print("even number of nodes")
        else:
            print("odd number of nodes")            
l1=sll()
l1.add_back(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.add_back(60)
l1.add_back(70)
l1.add_back(80)
#l1.add_front(5)
#l1.search(40)
l1.display()
#l1.remove_front()
print()
#l1.display()
l1.middle_node()
#l1.remove_back()
#l1.display()         



