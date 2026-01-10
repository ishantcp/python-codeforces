n=int(input())
r=0
if n%5==0:
    r=n//5
elif n%5==0 and n%4==0:
    r=n//5
elif n%5==0 and n%3==0:
    r=n//5
elif n%5==0 and n%2==0:
    r=n//5


else:
    r=(n//5)+1
print(r)