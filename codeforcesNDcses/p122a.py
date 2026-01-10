n = int(input())
lucky = [4, 7, 44, 47, 74, 77, 444, 447,477, 474, 744, 747,774, 777]
for L in lucky:
    if n % L == 0:
        print("YES")
        break
else:
    print("NO")