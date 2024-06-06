class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_back(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next

    def add_front(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            self.head.prev=node(x)
            self.head.prev.next=self.head
            self.head=self.head.prev
    
    def search(self,x):
        temp=self.head
        temp1=self.tail
        while temp!=temp1 and temp!=temp1.next:
            if temp.data==x or temp1.data==x:
                print(1)
                break
            temp=temp.next
            temp1=temp1.prev
        if temp.data==x:
            print(1)
        else:
            print(0)

    def length(self):
        temp=self.head
        temp1=self.tail
        while temp!=temp1 and temp!=temp1.next:
            temp=temp.next
            temp1=temp1.prev
        if temp==temp1:
            print("length:odd")
        else:
            print("length:even") 
    
    def check_pali(self):
        temp=self.head
        temp1=self.tail
        flag=1
        while temp!=temp1 and temp1.next!=temp:
            if temp.data!=temp1.data:
                flag=0
                #break
            temp=temp.next
            temp1=temp1.prev
        if flag and temp.data==temp1.data:
            print("yes palindrome")
        else:
            print("not a palindrome")
     


            
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"<->",end="")
            temp=temp.next



d1=dll()
d1.add_back(3)
d1.add_back(2)
d1.add_front(2)
d1.add_front(1)
d1.add_back(1)
d1.display()
print()
d1.search(6)
d1.length()
d1.check_pali()




