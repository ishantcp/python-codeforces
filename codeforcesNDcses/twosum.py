nums = list(map(int, input().split()))
t = int(input())

r = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == t:
            r.append((i, j))

print(r)
