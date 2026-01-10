n=int(input())
while n>0:
    n-=1
    a,b,c= map(int,input().split())
    if a<b and b<c:
        print("STAIR")
    elif a<b and b>c:
        print("PEAK")
    else:
        print("NONE")