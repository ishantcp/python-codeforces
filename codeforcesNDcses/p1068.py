n= int(input())
a=[]
a.append(n)
while n!=1:
    if n%2==0:
        n=n/2
        a.append(n)
        
    else:
        n=3*n+1
        a.append(n)
for x in a:
    print(int(x),end=' ')
    