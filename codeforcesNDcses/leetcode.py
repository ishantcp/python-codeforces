n= input()
t= int(input())
l=len(n)
for i in range(l):
    i+=1
    sum= n[0]+n[i]
    if sum==t:
        print(n[0],n[i])
        break
    elif sum!=t:
        continue
