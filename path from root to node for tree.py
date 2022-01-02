class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def roottonode(self,val,node,l):
        if val==None:
            return False
        l.append(val.data)
        if val.data==node:
            return True
        if self.roottonode(val.left,node,l) or self.roottonode(val.right,node,l):
            return True
        l.pop()
        return False
node=5
l=[]
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.left.right.left=Node(6)
t.root.left.right.right=Node(7)
t.roottonode(t.root,node,l)
print(l)
