n=input()
c=len(str(n))
count=0
for x in n:
    if x=='4':
        count+=1
        continue
    if x=='7':
        count+=1
        continue
if c%4==0:
    print("YES")
elif c%7==0:
    print("YES")
elif count==4:
    print("YES")
elif count==7:
    print("YES")
else:
    print("NO")