def dls(vis,a,r1,n,count,dl):
    if(count<dl):
        for i in range(0,n):
            if(a[r1][i]==1 and vis[i]==0):
                print(i,end=" ")
                vis[i]=1
                dls(vis,a,i,n,count+1,dl)
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
print("enter depth limit : ")
dlimit=int(input())
print(0,end=" ")
dls(vis,a,0,n,0,dlimit)