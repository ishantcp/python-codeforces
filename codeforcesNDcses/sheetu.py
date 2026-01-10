N = input().strip()

if '.' in N:
    integer_part, decimal_part = N.split('.')
    
    # check if decimal part is all zeros
    if int(decimal_part) == 0:
        print("int", integer_part)
    else:
        print("float", integer_part, "0."+decimal_part)
else:
    print("int", N)
