n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    u=int(input())
    v=int(input())
    adj[u].append(v)
print(adj)
queue=[]
res=[]
#level order
for i in range(1,n+1):
    queue.append(i)
    while queue!=[]:
        node=queue[0]
        queue.remove(queue[0])
        res.append(node)
        for k in adj[node]:
            queue.append(k)
    break
print(res)
res=[]
#pre order
def dfs(queue,node):
    res.append(node)
    if len(res)==n:
        return res
    for k in adj[node]:
        dfs(queue,k)
    return res
for i in range(1,n+1):
    queue.append(i)
    dfs(queue,i)
    break
print(res)
res=[]
#In order
def dfs(node):
    if len(res)==n:
        return res
    for k in adj[node]:
        dfs(k)
        if k not in res:
            res.append(k)
        if node not in res:
            res.append(node)
for i in range(1,n+1):
    dfs(i)
    break
print(res)
res=[]
#post order
def dfs(node):
    if len(res)==n:
        return res
    for k in adj[node]:
        dfs(k)
        res.append(k)
    return res
for i in range(1,n+1):
    dfs(i)
    res.append(i)
    break
print(res)
