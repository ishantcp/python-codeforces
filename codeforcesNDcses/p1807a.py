n=int(input())
r=[]
for i in range(n):
    n-=1
    a,b,c=map(int,input().split())
    if a+b==c:
        r.append("+")
    else:
        r.append("-")
for x in r:
    print(x)