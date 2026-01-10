n, k = map(int, input().split())
count = 0
a = list(map(int, input().split()))
if len(set(a)) == 1:
    print(len(a))
else:
    for x in a:     
        if x > k :    
            count+= 1
    print(count)
    