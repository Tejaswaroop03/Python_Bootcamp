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

    def pairs(self):
        l=[]
        temp=self.head
        while temp.nxt!=None:
            temp1=temp.nxt
            while temp1!=None:
                s=str(temp.data)+str(temp1.data)
                #l.append((temp.data,temp1.data))
                l.append(s)
                temp1=temp1.nxt
            temp=temp.nxt    
        print(l)        

    
    def bubble_sort(self):
        temp=self.head
        p=None
        while temp.nxt!=None:
            flag=0
            temp1=self.head
            while temp1.nxt!=p:
                if temp1.data>temp1.nxt.data:
                    flag=1
                    temp1.data,temp1.nxt.data=temp1.nxt.data,temp1.data
                temp1=temp1.nxt
            if flag==0:
                break
            p=temp1
            temp=temp.nxt

    def reverse(self):
        prev=None
        curr=self.head
        while(curr!=None):
            n=curr.nxt
            curr.nxt=prev
            prev=curr
            curr=n
        self.head=prev    


l1=sll()
l1.add_back(3)
l1.add_back(2)
l1.add_back(1)
l1.add_back(4)
l1.add_back(7)
l1.add_back(6)
l1.add_back(5)
l1.add_back(8)
l1.add_front(5)
l1.dispaly()
l1.search(40)
l1.display()
l1.remove_front()
print()
l1.display()
l1.middle_node()
l1.remove_back()
l1.display()
l1.pairs()
l1.bubble_sort()
l1.display()
l1.reverse()
print()
l1.display()         



