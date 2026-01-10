t=int(input())
r=[]
for i in range(t):
    a=list(map(int,input().split()))
    a.sort()
    r.append(a[1])
for x in r:
    print(x)
"completed"