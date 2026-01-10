matrix = []
a=0
b=0
r=0
for i in range(5):                      
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            a=i
            b=j
            break
r=abs(a-2)+abs(b-2)
print(r)
