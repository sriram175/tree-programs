n=int(input())
adj=[]
for i in range(n-1):
    l=list(map(int,input().split()))
    adj.append(l)
print(adj)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def insert(self,a,b,c):
        if self.root.data==a:
            if c==0:
                self.root.left=Node(b)
            else:
                self.root.right=Node(b)
        else:
            if c==0:
                a.left=Node(b)
            else:
                a.right=Node(b)
                print(a.data,a.left.data,a.right.data)
    def printf(self,val):
        if val!=None:
            print(val.data)
            self.printf(Node(val).left)
            self.printf(Node(val).right)
t=Tree(adj[0][0])
for i in adj:
    t.insert(Node(i[0]),Node(i[1]),Node(i[2]))
t.printf(Node(adj[0][0]))
