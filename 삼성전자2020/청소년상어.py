import copy

board = []
fish_loc = {}
for r in range(4):
    n_and_dir = list(map(int, input().split()))
    tmp = []
    for c, (i, j) in enumerate(zip([0, 2, 4, 6], [1, 3, 5, 7])):
        fish_loc[n_and_dir[i]] = (r, c)
        tmp.append((n_and_dir[i], n_and_dir[j]))  # n, dir
    board.append(tmp)

# board = [[(7, 6), (2, 3), (15, 6), (9, 8)],
#         [(3, 1), (1, 8), (1, 4), (7, 10)],
#         [(6, 1), (13, 6), (4, 3), (11, 4)],
#         [(16, 1), (8, 7), (5, 2), (12, 2)]]
#
# fish_loc = {7: (0, 0), 2: (0, 1), 15: (0, 2), 9: (0, 3), 3: (1, 0), 1: (1, 1), 14: (1, 2), 10: (1, 3), 6: (2, 0), 13: (2, 1), 4: (2, 2), 11: (2, 3), 16: (3, 0), 8: (3, 1), 5: (3, 2), 12: (3, 3)}

# direction :  1부터 순서대로 ↑, ↖, ←, ↙,  ↓, ↘, →, ↗
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1),
                        (1, 0), (1, 1), (0, 1), (-1, 1)]

# board[r][c] : (n,d)
# 빈칸 시 (0,0)

# 상어
"""
상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 
 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 
 물고기가 없는 칸으로는 이동할 수 없다. 
 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 
"""

# 물고기
"""
작은 물고기부터 이동.
물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 
 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
"""

# 1부터 순서대로 ↑, ↖, ←, ↙,  ↓, ↘, →, ↗
def move_fish(board, fish_loc: dict, shark_loc):
    s_r, s_c = shark_loc

    for fish in sorted(fish_loc):
        (r, c) = fish_loc[fish]
        (n, d) = board[r][c]

        for _ in range(8):
            d %= 8
            nr, nc = r + direction[d - 1][0], c + direction[d - 1][1]
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (s_r, s_c):  # 안막히고 상어 없으면 스왑
                board[r][c] = board[nr][nc] #board[nr][nc]
                board[nr][nc] = (n,d) #board[r][c] #swap

                fish_loc[n] = (nr, nc)
                if board[r][c][0] != 0:
                    n2 = board[r][c][0]
                    fish_loc[n2] = (r, c)

                break

            d += 1


# 어디 위치의 물고기를 먹었을 때 return n_of_fish to eat
max_fish_n = 0


def backtrack(board, fish_loc, cur_loc, cur_dir, cur_fishes):  # 현재 상어의 위치, 방향, 먹은개수주면 -> max_fish_n 을 업데이
    global max_fish_n

    candidates = []
    r, c = cur_loc
    dr, dc = direction[cur_dir - 1][0], direction[cur_dir - 1][1]


    nr, nc = r + dr, c + dc
    while 0 <= nr < 4 and 0 <= nc < 4:
        if board[nr][nc][0] != 0:
            candidates.append((nr, nc))
        nr, nc = nr + dr, nc + dc

    if not candidates:
        max_fish_n = max(max_fish_n, sum(cur_fishes))
        return

    for candidate in candidates:
        r, c = candidate
        n, next_dir = board[r][c]

        next_fish_loc = copy.deepcopy(fish_loc)
        del next_fish_loc[n]

        next_board = copy.deepcopy(board)
        next_board[r][c] = (0, 0)
        move_fish(next_board, next_fish_loc, (r, c))

        backtrack(next_board, next_fish_loc, (r,c), next_dir, cur_fishes + [n])

# 1부터 순서대로 ↑, ↖, ←, ↙,  ↓, ↘, →, ↗
n, dir = board[0][0]
del fish_loc[n]
board[0][0] = (0,0)
move_fish(board, fish_loc, (0, 0))

backtrack(board, fish_loc, (0, 0), dir, [n])
print(max_fish_n)

"""
board = [[(7, 6), (2, 3), (15, 6), (9, 8)], 
        [(3, 1), (1, 8), (1, 4), (7, 10)], 
        [(6, 1), (13, 6), (4, 3), (11, 4)], 
        [(16, 1), (8, 7), (5, 2), (12, 2)]]
        
fish_loc = {7: (0, 0), 2: (0, 1), 15: (0, 2), 9: (0, 3), 3: (1, 0), 1: (1, 1), 14: (1, 2), 10: (1, 3), 6: (2, 0), 13: (2, 1), 4: (2, 2), 11: (2, 3), 16: (3, 0), 8: (3, 1), 5: (3, 2), 12: (3, 3)}
"""
