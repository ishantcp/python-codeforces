n = int(input())         
all_lengths = []          
for _ in range(n):
    x, t = map(int, input().split())
    arr = list(range(1, x + 1))
    while len(arr) > t:
        arr.pop(t - 1)    
    all_lengths.append(len(arr))
for length in all_lengths:
    print(length)