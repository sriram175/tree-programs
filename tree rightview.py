class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def rightview(self,val,d,level):
        if val!=None:
            d[level]=val.data
            self.rightview(val.left,d,level+1)
            self.rightview(val.right,d,level+1)
        res=[]
        for i in sorted(d.keys()):
            res.append(d[i])
        return res
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.right=Node(7)
t.root.right.right.left=Node(6)
t.root.right.right.left.left=Node(8)
t.root.right.right.left.left.left=Node(9)
d={}
print(t.rightview(t.root,d,0))
