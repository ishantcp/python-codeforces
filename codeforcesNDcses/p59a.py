n=input()
upper=0
lower=0
for i in range(len(n)):
    if n[i].isupper():
        upper+=1
    else:
        lower+=1
if upper>lower:
    print(n.upper())
elif lower>upper:
    print(n.lower())
else:
    print(n.lower())