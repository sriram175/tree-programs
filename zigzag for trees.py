class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def zigzag(self,val,a,queue):
        queue.append(val)
        stack=[]
        while queue!=[]:
            size=len(queue)
            dummy=[]
            for i in range(size):
                node=queue[0]
                if a==0:
                    dummy.append(node.data)
                else:
                    dummy.insert(0,node.data)
                queue.remove(queue[0])
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            for i in dummy:
                stack.append(i)
            a=1-a
        return stack
queue=[]
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
print(t.zigzag(t.root,0,queue))
