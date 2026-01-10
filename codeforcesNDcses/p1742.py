t=int(input())
r=[]
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b==c or a+c==b or b+c==a:
        r.append("YES")
    else:
        r.append("NO")
for x in r:
    print(x)
