n=int(input())
a=input()
anton=0
danik=0
for x in a:
    if x=='A':
        anton+=1
    else:
        danik+=1
if anton>danik:
    print("Anton")
elif danik>anton:
    print("Danik")
else:
    print("Friendship")