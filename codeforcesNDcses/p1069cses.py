n=input()
cnta=0
cntc=0
cntg=0
cntt=0
for x in n:
    if x=='A':
        cnta+=1
    elif x=='C':
        cntc+=1
    elif x=='G':
        cntg+=1
    elif x=='T':
        cntt+=1
print(max(cnta,cntc,cntg,cntt))
"incomplete i have to count the continous repetion of a letter and print the result based on that"