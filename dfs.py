def dfs(vis,a,r1,n):
    for i in range(0,n):
        if(a[r1][i]==1 and vis[i]==0):
            print(i,end=" ")
            vis[i]=1
            dfs(vis,a,i,n)
print("Enter no of vertices : ")
n=int(input())
a=[]
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("Enter no of edgs : ")
edgs=int(input())
vis=[0]*n
print("Enter edges (src to dst) : ")
for i in range(0,edgs):
    l1,l2=map(int,input().split(' '))
    a[l1][l2]=1
print(0,end=" ")
dfs(vis,a,0,n)
