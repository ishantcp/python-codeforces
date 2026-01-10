n,h=map(int,input().split())
a=[]
count=0
for i in range(1,n):
    list(map(int, input().split()))
for j in range(0,n+1):
    if a[j]>h:
        count+=2
    else:
        count+=1
print(count)
