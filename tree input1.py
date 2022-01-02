class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self,root):
        self.root=Node(root)
    def insert(self,val,a):
        if val.data in a:
            val.left=Node(a[val.data][0])
            val.right=Node(a[val.data][1])
            self.insert(val.left,a)
            self.insert(val.right,a)
    def print(self,val):
        if val!=None:
            print(val.data,end=" ")
            self.print(val.left)
            self.print(val.right)
t=Tree(1)
n=int(input())
a={}
arr=[]
for i in range(n-1):
    l=list(map(int,input().split()))
    arr.append(l)
for x,y,z in arr:
    if x not in a:
        if z==0:
            a[x]=[y,0]
        else:
            a[x]=[0,y]
    else:
        if z==0:
            a[x][0]=y
        else:
            a[x][1]=y
t.insert(t.root,a)
t.print(t.root)
