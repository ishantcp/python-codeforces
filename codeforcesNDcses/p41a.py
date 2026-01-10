s = input().strip()
t = input().strip()

if len(s) != len(t):
    print("NO")
else:
    for i in range(len(s)):
        if s[i] != t[len(t)-1-i]:
            print("NO")
            break
    else:
        print("YES")