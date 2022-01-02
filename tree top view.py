class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def topview(self,val):
        queue=[(0,val)]
        d={}
        res=[]
        stack=[]
        while queue!=[]:
            node=queue[0]
            queue.remove(queue[0])
            if node[0] not in d:
                d[node[0]]=node[1].data
            if node[1].left!=None:
                a=node[0]-1
                b=node[1].left
                c=(a,b)
                queue.append(c)
            if node[1].right!=None:
                a=node[0]+1
                b=node[1].right
                c=(a,b)
                queue.append(c)
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
t.root.left.right.left=Node(6)
t.root.left.right.left.left=Node(8)
t.root.left.right.left.left.left=Node(9)
print(t.topview(t.root))
