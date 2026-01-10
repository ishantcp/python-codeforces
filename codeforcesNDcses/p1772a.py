t=int(input())
a=0
b=0
c=0
r=[]
for i in range(t):
    s=input()
    a=int(s[0])
    b=int(s[-1])
    c=a+b
    r.append(c)
for x in r:
    print(x)