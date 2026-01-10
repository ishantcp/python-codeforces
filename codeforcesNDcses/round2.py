n, k = map(int, input().split())
a = list(map(int, input().split()))

threshold = a[k - 1] if 1 <= k <= n else 0  # k is 1-based
count = 0
for x in a:
    if x > 0 and x >= threshold:
        count += 1

print(count)