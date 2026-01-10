z = int(input())
r=[]

for _ in range(z):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)

    if a == b or k > 1:
        r.append("YES")
    else:
        r.append("NO")
for x in r:
    print(x)
