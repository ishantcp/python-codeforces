'multiply by two if n%6!=0'
'and divide by 6 if n%6==0'
n=int(input())
count=0
while n>0:
    n-=1
    a=int(input())
    while a!=1:
        if a%6==0:
            a=a/6
            count+=1
        elif a%6!=0:
            a=a*2
            count+=1
        elif a==1:
            print(count)
            break
        else:
            print("-1")
            break
    print(count)
