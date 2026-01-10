a,b,c,d=map(int,input().split())
x=[]
x.append(a)
x.append(b)
x.append(c)
x.append(d)
z=set(x)
print(4-len(z))