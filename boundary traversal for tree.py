class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def isleaf(self,val):
        if val.left==None and val.right==None:
            return True
    def leftboundary(self,val,ans):
        cur=val.left
        while cur:
            if (self.isleaf(cur)!=True):
                ans.append(cur.data)
            if cur.left!=None:
                cur=cur.left
            else:
                cur=cur.right
    def rightboundary(self,val,ans):
        res=[]
        cur=val.right
        while cur:
            if (self.isleaf(cur)!=True):
                res.append(cur.data)
            if (cur.right!=None):
                cur=cur.right
            else:
                cur=cur.left
        for i in res[::-1]:
            ans.append(i)
    def leafboundary(self,val,ans):
        if self.isleaf(val):
            ans.append(val.data)
        if val.left!=None:
            self.leafboundary(val.left,ans)
        if val.right!=None:
            self.leafboundary(val.right,ans)
    def boundary(self,val):
        ans=[]
        if val==None:
            return ans
        if self.isleaf(val)!=True:
            ans.append(val.data)
        self.leftboundary(val,ans)
        self.leafboundary(val,ans)
        self.rightboundary(val,ans)
        return ans
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(7)
t.root.left.left=Node(3)
t.root.left.left.right=Node(4)
t.root.left.left.right.left=Node(5)
t.root.left.left.right.right=Node(6)
t.root.right.right=Node(8)
t.root.right.right.left=Node(9)
t.root.right.right.left.left=Node(10)
t.root.right.right.left.right=Node(11)
print(t.boundary(t.root))
