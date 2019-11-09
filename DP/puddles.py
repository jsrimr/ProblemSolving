from collections import namedtuple
from copy import deepcopy as deepcopy
answer = 0
Position = namedtuple("position", "x y")


def solution(m, n, puddles):
    array = [[1 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(n + 2):
        if i == 0 or i == n+1:
            for j in range(m + 2):
                array[i][j] = -1
        else:
            array[i][0] = -1
            array[i][m+1] = -1
    for pud in puddles:
        x = pud[0]
        y = pud[1]
        array[x][y] = -1

    def backtrack(cur, array):
        global answer
        # 종료조건 : 사방이 막혔거나 , goal 에 도달했을떄 , | -> 지나온 지점도 -1 로 표시해야함
        if cur.x == m and cur.y == n:
            answer += 1
            return
        if array[cur.y][cur.x + 1] == -1 and array[cur.y + 1][cur.x] == -1 and array[cur.y][cur.x - 1] == -1 and \
                array[cur.y - 1][cur.x] == 1:
            return
        # x 쪽 방향으로 한칸 전진 가능 | 지나온 지점 -1 로 표시 , recursive call | cache 에 경로 추가
        if array[cur.y][cur.x + 1] != -1:
            new_array = deepcopy(array)
            new_array[cur.y][cur.x] = -1
            new_cur = Position(cur.x+1, cur.y)

            # path = path+[new_cur]
            # cache.add(path)
            backtrack(new_cur, new_array)

        # y 쪽 방향으로 한칸 전진 가능
        if array[cur.y + 1][cur.x] != -1:
            new_array = deepcopy(array)
            new_array[cur.y][cur.x] = -1
            new_cur = Position(cur.x, cur.y+1)

            # path = path + [new_cur]
            # cache.add(path)
            backtrack(new_cur, new_array)

        # x, y 둘다 막혔고 왔던 방향말고 한 군데 남은 경우
        if array[cur.y + 1][cur.x] == -1 and array[cur.y][cur.x + 1] == -1:
            new_array = deepcopy(array)
            new_array[cur.y][cur.x] = -1


            if array[cur.y - 1][cur.x] != -1:
                new_cur = Position(cur.x, cur.y-1)
                # new_cur.y -= 1
                backtrack(new_cur, new_array)

            elif array[cur.y][cur.x - 1] != -1:
                new_cur = Position(cur.x-1, cur.y)
                # new_cur.x -= 1
                backtrack(new_cur, new_array)
            # path = path + [new_cur]
            # cache.add(path)

    cur = Position(1, 1)
    backtrack(cur, array)

    return answer % 1000000007


print(solution(4, 4, [[2, 2],[2,3],[2,4],[4,1],[4,2]]))
