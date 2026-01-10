n= int(input())
count=0
z=0
a=list(map(int,input().split()))
s=sorted(a)
median= len(a)//2
for x in a:
    if x<s[median]:
        z= s[median]-x
        count+=z
    elif x>s[median]:
        z=x-s[median]
        count+=z
print(count)