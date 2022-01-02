class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def height(self,val):
        queue=[]
        queue.append(val)
        count=0
        while queue!=[]:
            size=len(queue)
            for i in range(size):
                node=queue[0]
                queue.remove(queue[0])
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            count+=1
        return count
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.left.left=Node(5)
t.root.left.left.left.left=Node(6)
t.root.right.right=Node(7)
print(t.height(t.root))
