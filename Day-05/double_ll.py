from math import sqrt
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
        while temp!=temp1 or temp1.next!=temp:
            if temp.data!=temp1.data:
                flag=0
                #break
            temp=temp.next
            temp1=temp1.prev
        if flag and temp.data==temp1.data:
            print("yes palindrome")
        else:
            print("not a palindrome")
     
    def rotate(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        self.tail.next=self.head
        self.head.prev=self.tail
        slow.prev.next=None
        slow.prev=None
        self.head=slow 

    def even_odd_sum(self):
        temp=self.head
        '''def rec(temp,even_sum,odd_sum):
            if temp==None:
                return(abs(even_sum-odd_sum))
            if(temp.data%2==0):
                even_sum+=temp.data
            else:
                odd_sum+=temp.data
            return rec(temp.next,even_sum,odd_sum)
        print(rec(temp,0,0))'''

        temp1=self.tail
        def rec1(temp,temp1,sum):
            if temp==temp1 or temp1.next==temp:
                if temp==temp1:
                    if temp.data%2==0:
                        sum+=temp.data
                    else:
                        sum-=temp.data    
                return abs(sum)
            if(temp.data%2==0):
                sum+=temp.data
            else:
                sum-=temp.data
            if(temp1.data%2==0):
                sum+=temp1.data
            else:
                sum-=temp1.data
            print(temp.data,temp1.data,sum)    
            return rec1(temp.next,temp1.prev,sum)
        print(rec1(temp,temp1,0))

    def count_prime(self,temp,count):
        temp=self.head
        if temp==None:
            return count
        def check_prime(n):
            for i in range(2,sqrt(n)+1):
                if n%i!=0:
                    return False
            return True
        count+=check_prime(temp.data)
        return count_prime(temp.next,count)
        
        
        
             



       
                   

                
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"<->",end="")
            temp=temp.next



d1=dll()
#d1.add_back(3)
d1.add_back(5)
d1.add_back(7)
d1.add_back(8)
d1.add_back(9)
d1.add_back(10)
d1.add_back(12)
d1.add_back(15)
d1.display()
print()
#d1.search(6)
#d1.length()
#d1.check_pali()
#d1.rotate()
d1.even_odd_sum()
d1.display()





