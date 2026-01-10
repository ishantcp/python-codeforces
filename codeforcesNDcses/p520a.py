N=int(input())
s = input().lower()

alphabets = set("abcdefghijklmnopqrstuvwxyz")

if alphabets.issubset(set(s)):
    print("YES")
else:
    print("NO")