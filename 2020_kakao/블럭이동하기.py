def arrived(r, c, n):
    return (r == n - 1) or (c == n - 1)


def to_up(r, c, d, n):
    if d == 1:
        if r - 1 >= 0 and board[r - 1][c] == 0 and board[r - 1][c + 1] == 0:
            return (r - 1, c, d)
    elif d == 2:
        if r - 2 >= 0 and board[r - 2][c] == 0:
            return (r - 1, c, d)
    elif d == 3:
        if r - 1 >= 0 and c - 1 >= 0 and board[r - 1][c] == 0 and board[r - 1][c - 1] == 0:
            return (r - 1, c, d)
    else:
        if r - 1 >= 0 and board[r - 1][c] == 0:
            return (r - 1, c, d)


def to_right(r, c, d, n):
    if d == 1:
        if c + 2 <= n - 1 and board[r][c + 2] == 0:
            return (r, c + 1, d)
    elif d == 2:
        if c + 1 <= n - 1 and board[r][c + 1] == 0 and board[r - 1][c + 1] == 0:
            return (r, c + 1, d)
    elif d == 3:
        if c + 1 <= n - 1 and board[r][c + 1] == 0:
            return (r, c + 1, d)
    else:
        if c + 1 <= n - 1 and board[r][c + 1] == 0 and board[r + 1][c + 1] == 0:
            return (r, c + 1, d)


def to_down(r, c, d, n):
    if d == 1:
        if r + 1 <= n - 1 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
            return (r + 1, c, d)
    elif d == 2:
        if r+1 <=n-1 and board[r+1][c] == 0:
            return (r + 1, c, d)
    elif d == 3:
        if r + 1 <= n - 1 and board[r + 1][c] == 0 and board[r + 1][c - 1] == 0:
            return (r + 1, c, d)
    else:
        if r + 1 <= n - 1 and board[r + 1][c] == 0:
            return (r + 1, c, d)


def to_left(r, c, d, n):
    if d == 1:
        if c-1 >=0 and board[r][c-1] == 0:
            return (r, c - 1, d)
    elif d == 2:
        if c-1 >=0 and board[r][c-1] == 0 and board[r - 1][c-1] == 0:
            return (r, c - 1, d)
    elif d == 3:
        if c-1 >=0 and board[r][c-1] == 0:
            return (r, c - 1, d)
    else:
        if c-1 >=0 and board[r][c-1] == 0 and board[r + 1][c-1] == 0:
            return (r, c - 1, d)


def x_to_clock(r, c, d, n):
    if d == 1:
        if r+1 <= n-1 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            return (r-1, c + 1, 2)
    elif d == 2:
        if c + 1 <= n-1 and board[r][c + 1] == 0 and board[r - 1][c + 1] == 0:
            return (r-1, c + 1, 3)
    elif d == 3:
        if r-1 >=0 and board[r-1][c]==0 and board[r-1][c-1]==0:
            return (r-1, c - 1, 4)
    else:
        if c - 1 >= 0 and board[r][c - 1] == 0 and board[r + 1][c - 1] == 0:
            return (r+1, c - 1, 1)

def x_to_counterClock(r, c, d, n):
    if d == 1:
        if r+1 <= n-1 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            return (r-1, c + 1, 2)
    elif d == 2:
        if c + 1 <= n-1 and board[r][c + 1] == 0 and board[r - 1][c + 1] == 0:
            return (r-1, c + 1, 3)
    elif d == 3:
        if r-1 >=0 and board[r-1][c]==0 and board[r-1][c-1]==0:
            return (r-1, c - 1, 4)
    else:
        if c - 1 >= 0 and board[r][c - 1] == 0 and board[r + 1][c - 1] == 0:
            return (r+1, c - 1, 1)

def y_to_clock(r, c, d, n):
    pass


def y_to_counterClock(r, c, d, n):
    pass


def solution(board):
    r, c, d = 0, 0, 1
    n = len(board)
    queue = []
    answer = 0
    while queue:
        (r, c, d) = queue.pop()
        if arrived(r, c, n):
            break
        for ret in [to_up(r, c, d, n), to_right(r, c, d, n), to_down(r, c, d, n), to_left(r, c, d, n),
                    x_to_clock(r, c, d, n), x_to_counterClock(r, c, d, n), y_to_clock(r, c, d, n),
                    y_to_counterClock(r, c, d, n)]:  # 상하좌우, x를 축으로 회전방향2, y를 축으로 회전방향2
            if ret: queue.append(ret)
        answer += 1

    return answer


# bfs 문제

if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    print(solution(board))
