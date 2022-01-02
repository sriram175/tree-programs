class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def identical(self,val,l):
        if val!=None:
            l.append(val.data)
            self.identical(val.left,l)
            self.identical(val.right,l)
        return l
t1=Tree(1)
l1=[]
l2=[]
t1.root.left=Node(2)
t1.root.right=Node(3)
t1.root.left.left=Node(4)
t1.root.left.right=Node(5)
t1.root.right.left=Node(6)
t1.root.right.right=Node(7)
t2=Tree(1)
t2.root.left=Node(2)
t2.root.right=Node(3)
t2.root.left.left=Node(4)
t2.root.left.right=Node(5)
t2.root.right.left=Node(6)
t2.root.right.right=Node(7)
if t1.identical(t1.root,l1)==t2.identical(t2.root,l2):
    print("Identical")
else:
    print("Non Identical")
