class Node:
    def __init__(self, x) -> None:
        self.data = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        else:
            if x < root.data:
                root.left = self.create(root.left, x)
            else:
                root.right = self.create(root.right, x)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def add_nodes(self,root):
        if root is None:
            return 0
        '''else:
            left=self.add_nodes(root.left)
            right=self.add_nodes(root.right)
            return root.data+left+right'''
        return root.data+self.add_nodes(root.left)+self.add_nodes(root.right)
    def add_even(self,root):
        if root is None:
            return 0
        if(root.data%2==0):
            return root.data+self.add_even(root.left)+self.add_even(root.right)
        else:
            return self.add_even(root.left)+self.add_even(root.right)

    def diff(self,root):
        if root is None:
            return 0
        if(root.data%2==0):
            return root.data+self.diff(root.left)+self.diff(root.right)
        return self.diff(root.left)+self.diff(root.right)-root.data
    
    def height(self,root):
        if(root==None):
            return -1
        return max(self.height(root.left),self.height(root.right))+1

    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))
    
    def leaf_nodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leaf_nodes(root.left)+self.leaf_nodes(root.right)
    
    def sum_leaf_nodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.sum_leaf_nodes(root.left)+self.sum_leaf_nodes(root.right)
    
    def search(self,root,x):
        if root==None:
            return False
        if root.data==x:
            return True
        if root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)

    def depth(self,root,y,c):
        if(root==None):
            return -1
        if(root.data==y):
            return c
        if(root.data>y):
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)

    def left_view(self,root):
        if root==None:
            return
        print(root.data,end="")
        self.left_view(root.left)

        
    

     
t1=Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 2)
t1.root = t1.create(t1.root, 9)
t1.root=t1.create(t1.root,1)
t1.root=t1.create(t1.root,25)
print("inorder:",end=" ")
t1.inorder(t1.root)
print()
print("preorder:",end=" ")
t1.preorder(t1.root)
print()
print("postorder:",end=" ")
t1.postorder(t1.root)
print()
print("sum of nodes:",t1.add_nodes(t1.root))
print("sum of even nodes:",t1.add_even(t1.root))
print("absolute diff of even and odd :",t1.diff(t1.root))
print("height od the tree:",t1.height(t1.root))
if(t1.balance(t1.root)<=1):
    print("balanced tree")
else:
    print("unbalanced tree")
print("n.o of leaf nodes:",t1.leaf_nodes(t1.root))
print("sum of leaf nodes:",t1.sum_leaf_nodes(t1.root))      
print("search for an element:",t1.search(t1.root,1))
print("depth:",t1.depth(t1.root,1,0))
t1.left


