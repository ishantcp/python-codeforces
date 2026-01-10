n=int(input())
while n>0:
    n-=1
    a=map(int,input().split())
    if 1 in a:
        print("HARD")
        break
    else:
        print("EASY")
        break