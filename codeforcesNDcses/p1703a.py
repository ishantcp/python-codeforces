t = int(input())
r = []

for i in range(t):
    s = input().strip()
    if s.lower() == "yes":
        r.append("YES")
    else:
        r.append("NO")

for x in r:
    print(x)
