a,b,c,d= int(input()), int(input()), int(input()), int(input())
print(a, b, c, d)
if a==c and b==d:
        print("NO")
elif c-a < d-b:
        print("NO")
elif b-a == d-c:
        print("YES")
elif c-a > d-b:
        print("YES")
elif c-a == d-b:
        print("YES")
elif b-a < d-c:
        print("NO")
else:
        print("NO")

