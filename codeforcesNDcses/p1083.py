n=int(input())
a=map(int,input().split())
a=set(a)
z=0
for i in range(1,n+1):
    if i  in a:
        continue
    else:
        z=i
        break
print(z)
