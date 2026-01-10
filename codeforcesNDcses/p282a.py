n=int(input())
a=0
b=0
while n>0:
    n-=1
    x=input()
    if x=="++X" or x=="X++":
        a+=1
    elif x=="--X" or x=="X--":
        b+=1
print(a-b)