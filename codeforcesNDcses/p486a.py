n=int(input())
a,b=0,0
for i in range(1,n+1):
        if i%2!=0:
            a=a+i
            print("a",a)
        else:
            b=b+i
            print("b",b)
print(b-a)
'''n=int(input())
a,b=0,0
while n>0:
    n-=1
    if n%2==0:
        a-=n
    elif n%2!=0:
        b+=n
print(a+b)

n = int(input())
m = n - 1
odd_count = (m + 1) // 2
even_count = m // 2
odd_sum = odd_count * odd_count
even_sum = even_count * (even_count + 1)
print(odd_sum - even_sum)'''

