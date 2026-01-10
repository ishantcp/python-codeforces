n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

r = []

for i in range(len(arr)):
    if arr[i] <= 1399:
        r.append("Division 4")
    elif arr[i] <= 1599:
        r.append("Division 3")
    elif arr[i] <= 1899:
        r.append("Division 2")
    else:
        r.append("Division 1")

for y in r:
    print(y)
