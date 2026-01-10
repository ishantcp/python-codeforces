t=int(input())
s=[1,2,3,4,5,6,7,8,9]
count=0
r=[]
for i in range(t):
    n=int(input())
    for j in range(1,n):
        if s[j]+s[j]==n:
            count+=1
        elif s[j]+s[j-1]==n:
            count+=1
        elif s[j]+s[j+1]==n:
            count+=1
    r.append(count)
for x in r:
    print(x)