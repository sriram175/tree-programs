from queue import PriorityQueue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def verticaltraversal(self,val):
        queue=[]
        stack=PriorityQueue()
        a=(0,0,val)
        queue.append(a)
        while queue!=[]:
            node=queue[0]
            a=node[0]
            b=node[1]
            c=node[2]
            d=(a,b,c.data)
            stack.put_nowait(d)
            queue.remove(queue[0])
            if node[2].left!=None:
                a=node[0]-1
                b=node[1]+1
                c=node[2].left
                d=(a,b,c)
                queue.append(d)
            if node[2].right!=None:
                a=node[0]+1
                b=node[1]+1
                c=node[2].right
                d=(a,b,c)
                queue.append(d)
        res=[]
        while stack.qsize()!=0:
            node=stack.get_nowait()
            res.append(node[2])
        return res
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(10)
t.root.right.left=Node(9)
t.root.right.right=Node(10)
t.root.left.left.right=Node(5)
t.root.left.left.right.right=Node(6)
print(t.verticaltraversal(t.root))
