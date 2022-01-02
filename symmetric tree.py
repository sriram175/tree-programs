class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def symmetric(self,root):
        if root==None:
            return True
        return self.issymmetric(root.left,root.right)
    def issymmetric(self,left,right):
        if left==None or right==None:
            return left==right
        if left.data!=right.data:
            return False
        return self.issymmetric(left.left,right.right) and self.issymmetric(left.right,right.left)
l1=[]
l2=[]
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(2)
t.root.left.right=Node(3)
t.root.right.left=Node(3)
if t.symmetric(t.root):
    print("Symmetric")
else:
    print("Non symmetric")
