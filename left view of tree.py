class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    #using iteration
    def leftview(self,val):
        queue=[]
        a=(0,0,val)
        queue.append(a)
        d={}
        while queue!=[]:
            node=queue[0]
            queue.remove(queue[0])
            if node[0]  not in d:
                d[node[0]]=node[2].data
            if node[2].left!=None:
                a=node[0]+1
                b=node[1]-1
                c=node[2].left
                queue.append((a,b,c))
            if node[2].right!=None:
                a=node[0]+1
                b=node[1]+1
                c=node[2].right
                queue.append((a,b,c))
        res=[]
        for i in sorted(d.keys()):
            res.append(d[i])
        return res
    #using recursion
    def leftview2(self,val,d,level):
        if val!=None:
            if level not in d:
                d[level]=val.data
            self.leftview2(val.left,d,level+1)
            self.leftview2(val.right,d,level+1)
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
print(t.leftview(t.root))
d={}
print(t.leftview2(t.root,d,0))
