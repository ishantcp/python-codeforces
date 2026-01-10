t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    dot_count = s.count('.')
    found_three = False

    for i in range(n - 2):
        if s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
            found_three = True
            break

    if dot_count == 0:
        print(0)
    elif found_three:
        print(2)
    else:
        print(dot_count)
