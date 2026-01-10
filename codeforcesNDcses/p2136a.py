n=int(input())
r=[]
for i in range(n):
    a,b,c,d=map(int,input().split())
    y=c-a
    z=d-b
    if max(a,b)<=(2*min(a,b))+2 and max(y,z)<=(2*min(y,z))+2:
        r.append("YES")
    else:
        r.append("NO")
for x in r:
    print(x)