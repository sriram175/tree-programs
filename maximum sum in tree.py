class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def maxsum(self,val,l):
        if val==None:
            return 0
        lh=self.maxsum(val.left,l)
        rh=self.maxsum(val.right,l)
        if lh<0:
            lh=0
        if rh<0:
            rh=0
        l[0]=max(l[0],lh+rh+val.data)
        return val.data+max(lh,rh)
    def result(self,val,l):
        self.maxsum(val,l)
        return l[0]
t=Tree(-10)
l=[0]
t.root.left=Node(9)
t.root.right=Node(-20)
t.root.right.left=Node(-30)
t.root.right.right=Node(15)
print(t.result(t.root,l))
