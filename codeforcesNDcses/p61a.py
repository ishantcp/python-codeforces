s=input()
r=input()
ln=len(s)
a=[]
for i in range(ln):
    if s[i]!=r[i]:
        a.append(1)
    else:
        a.append(0)
for x in a:
    print(x,end="")
