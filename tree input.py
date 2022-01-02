n=int(input())
arr=[]
for i in range(n-1):
    l=list(map(int,input().split()))
    arr.append(l)
d={}
for x,y,z in arr:
    if x not in d:
        if z==0:
            d[x]=[y,0]
        else:
            d[x]=[0,y]
    else:
        if z==0:
            d[x][0]=y
        else:
            d[x][1]=y
print(d)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def insert(self,node):
        if node!=None:
            if node.data in d:
                node.left=Node(d[node.data][0])
                node.right=Node(d[node.data][1])
                self.insert(node.left)
                self.insert(node.right)
    def print(self,val):
        if val!=None:
            print(val.data,end=" ")
            self.print(val.left)
            self.print(val.right)
t=Tree(1)
t.insert(t.root)
t.print(t.root)
