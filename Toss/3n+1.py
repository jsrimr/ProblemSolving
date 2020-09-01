def cypro(n, b, c):
    cl = 1
    proc = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            cl += 1
            proc.append(n)
        else:
            n = 3 * n + 1
            if n > b / 3 and c > 0:
                n += 10
                c -= 1
            cl += 1
            proc.append(n)
    return cl


# user_input = input()
# a, b, c = map(int, user_input.split())
a, b, c = (153, 200, 1)
a, b, c = (22,22,3)
arw = []
for n in range(a, b + 1):
    arw.append(cypro(n, b, c))
print(max(arw))
