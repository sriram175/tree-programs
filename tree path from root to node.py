class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def path(self,node,val,l):
        if node!=None:
            l.append(node.data)
            if node.data==val:
                return True
            if self.path(node.left,val,l) or self.path(node.right,val,l):
                return True
            l.pop()
        return False
node=9
l=[]
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
t.root.right.right.left=Node(8)
t.root.right.right.right=Node(9)
t.path(t.root,node,l)
print(l)


    
