def num(a):
    b=a//10
    c=a%10
    sum=b+c
    r.append(sum)
n=int(input())
r=[]
for i in range(n):
    x=int(input())
    num(x)
for y in r:
    print(y)
"completed;)"