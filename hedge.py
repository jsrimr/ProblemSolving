straight = 100000
hedge = 100000
r = 0.1
for i in range(100):
    print(sum([straight, hedge]))
    if i % 4 != 0:
        straight *= (1 + r)
        hedge *= (1 - r)
    else:
        straight *= (1 - r)
        hedge *= (1 + r)

-float("INF")