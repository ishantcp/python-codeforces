n=int(input())
s="codeforces"
count=0
while n>0:
    n-=1
    a=list(map(input().split()))    
    for i in range(10):
        if s[i]==a[i]:
            count+=0
            continue
        else:
            count+=1
print(count)
