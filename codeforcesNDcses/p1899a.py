t=int(input())
r=[]
for i in range(t):
    a=int(input())
    if a==1:
        r.append("First")
    else:
        for j in range(1,11):
            a+=1
            if a%3==0 and j%2==0:
                r.append("First")
                break
            elif a%3==0 and j%2!=0:
                r.append("Second")
            else:
                continue
        r.append("Second")
        break
for x in r:
    print(x)


