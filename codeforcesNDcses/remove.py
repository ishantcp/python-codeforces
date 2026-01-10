n = int(input())
while n > 0:
    n -= 1
    x, y = map(int, input().split())
    a = []
    for i in range(1, x + 1):
        a.append(i)
print(a)
    