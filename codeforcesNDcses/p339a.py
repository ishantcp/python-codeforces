n=input()
s=sorted(n)
r=[]
for x in s:
    if x.isdigit():
        r.append(x)
print("+".join(r))

