import copy
import time
from collections import defaultdict

N, M, K = map(int, input().split())  # N 개에 걸쳐 격자의 모습,
# 상어개수 M , k번 이동하면 냄새 사라

board = []
shark_info = {}  # 1 : [r,c,d],  위치와 방향

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] != 0:
            shark_info[row[j]] = [i, j]
    board.append(row)

shark_directions = map(int, input().split())
for i, d in enumerate(shark_directions):
    shark_info[i + 1].append(d)

shark_priorities = defaultdict(list)
for i in range(M):
    for _ in range(4):
        pr = map(int, input().split())
        shark_priorities[i + 1].append(list(pr))

answer = 0
for shark, info in shark_info.items():
    r, c, d = info
    board[r][c] = [shark, K, d]  # [1,k, d] 등으로 상어와 남은시간과 방향표시

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 1 2 3 4 : 위 아래 왼쪽 오른쪽

"""
맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 
자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 
우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
"""

"""
board = []
shark_info = {} # 1 : [r,c,d],  위치와 방향 
shark_priorities = defaultdict(list) : [[2 3 1 4], [4,1,2,3]...]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
"""


def count_down_scent():
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and len(board[i][j]) == 2:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = 0

# 1 2 3 4 : 위 아래 왼쪽 오른쪽
def find_back(shark, r, c, board):
    if 0 <= r - 1 < N and 0 <= c < N and board[r - 1][c][0] == shark:
        return r - 1, c, 1

    if 0 <= r + 1 < N and 0 <= c < N and board[r + 1][c][0] == shark:
        return r + 1, c, 2

    if 0 <= r < N and 0 <= c - 1 < N and board[r][c - 1][0] == shark:
        return r, c - 1, 3

    if 0 <= r < N and 0 <= c + 1 < N and board[r][c + 1][0] == shark:
        return r, c + 1, 4


# (s,K,d)
def find_sharks():
    sharks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and len(board[i][j]) == 3:
                sharks.append((board[i][j][0], i, j, board[i][j][2]))
    return sharks


def move_shark():
    copied_board = copy.deepcopy(board)
    sharks = find_sharks()
    for s, r, c, d in sorted(sharks, reverse=True):
        # r, c, d = shark_info[s]

        prs = shark_priorities[s][d - 1]
        for d in prs:
            dr, dc = directions[d - 1]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and copied_board[nr][nc] == 0:
                break

        else:  # 자기 냄새 있는곳으로 돌아가기
            nr, nc, d = find_back(s, r, c, copied_board)

        board[r][c] = board[r][c][:2]
        board[nr][nc] = [s, K, d]

def check_only_one_shark():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and len(board[i][j]) == 3:
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False

# 1 2 3 4 : 위 아래 왼쪽 오른쪽
start_time = time.time()
while True:
    move_shark()
    count_down_scent()  # k 모두 -1
    answer += 1
    if check_only_one_shark():
        print(answer)
        break

    if time.time() - start_time > 1:
        print(-1)
        break