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

t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 2)
t1.root = t1.create(t1.root, 9)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)


