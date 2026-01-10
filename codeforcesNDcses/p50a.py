m,n=map(int,input().split())
r=0
if m*n%2==0:
    r=m*n//2
else:
    r=(m*n)//2
print(r)