n=input()
ln=len(n)
a=[2,3,4,5,6,7,8,9]
b=[]
for i in range(ln):
    if a[i]==n[i]:
        continue
    else:
        b.append(a[i])
for y in b:
    print(y,end="")