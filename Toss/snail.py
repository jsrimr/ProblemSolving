# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# # user_input = input()
# # k, n = map(int, user_input.split())


def snail(k,n):
    array = [[0 for j in range(n)] for i in range(n)]
    directions = [
        lambda i, j: (i, j + 1),
        lambda i, j: (i + 1, j),
        lambda i, j: (i, j - 1),
        lambda i, j: (i - 1, j),
    ]

    def in_matrix(i, j):
        return 0 <= i < n and 0 <= j < n

    def is_visited(i, j):
        return array[i][j] != 0

    direction_cnt = 0
    if k == 1:
        i,j = (0, 0)
    elif k == 2:
        i,j = (0, n-1)
    elif k == 3:
        i,j = (n-1, n-1)
    else:
        i,j = (n-1, 0)
    cnt = 1
    array[i][j] = cnt  # mark as visited
    while True:

        direction_func = directions[direction_cnt % 4]  # turning directions in circle
        tmp_i, tmp_j = direction_func(i, j)  # attempt to head one step
        if (not in_matrix(tmp_i, tmp_j)) or is_visited(tmp_i, tmp_j):  # over border or visted
            direction_cnt += 1  # change direction
        else:
            cnt += 1
            i, j = tmp_i, tmp_j  # confirm this step
            array[i][j] = cnt  # mark as visited
            if cnt == n**2:  # simple terminal criteria
                return array


if __name__ == '__main__':
    k=1
    n=5
    ret = snail(k,n)
    # print(ret)
    s = ""
    for row in ret:
        for i,el in enumerate(row):
            if (i+1) % n == 0:
                s += f"{el:5d}"+"\n"
            else:
                s += f"{el:5d}"
    print(s)
