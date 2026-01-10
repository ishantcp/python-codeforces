n, k = map(int, input().split())
count = 0
a = list(map(int, input().split()))
if set(a) == {0}:
    print(0)
elif len(set(a)) == 1:
    print(len(a))

else:
    for x in a:
        if x==0:
            continue   
        if x >= a[k-1] :    
            count+= 1
        
    print(count)
    