g, c, l = map(int, input().split())
maximum = max(g, c, l)
minimum = min(g, c, l)
if maximum - minimum >= 10:
    print("check again")
else:   
    scores = sorted([g, c, l])
    print("final", scores[1])
