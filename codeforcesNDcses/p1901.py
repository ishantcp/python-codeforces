t=int(input())
dist=[]
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    ans=a[0]
    for j in range(1,n):
        ans=max(ans,a[j]-a[j-1])
        continue
    ans=max(ans,2*(x-a[-1]))
    dist.append(ans)
for z in dist:
    print(z)

    