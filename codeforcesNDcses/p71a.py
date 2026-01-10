n=int(input())
while n>0:
    n-=1
    a =input()
    c = len(a)
    if c > 10:
        print(a[0], c-2, a[-1], sep="") 
    elif c<=10:
        print(a)
          