n = int(input())
results = []
while n > 0:
    n -= 1
    a, b = map(int, input().split())
    if a % b == 0:
        results.append(0)
    else:
        results.append(b - (a % b))
for r in results:
    print(r)
