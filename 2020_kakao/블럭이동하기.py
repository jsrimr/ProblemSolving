def arrived(x, y, n):
    return (x == n - 1) or (y == n - 1)


# x 가 row ,y 가 열
def backtrack(x1, y1, x2, y2, cnt, state, board):
    n = len(board)
    if state == "가로":
        if not arrived:
            if y2 + 1 < n and board[x2][y2 + 1] != 1:
                a1 = backtrack(x1, y1 + 1, x2, y2 + 1, cnt + 1, "가로", board)  # right
            if x1 + 1 < n and x2 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                a2 = backtrack(x1 + 1, y1, x2 + 1, y2, cnt + 1, "가로", board)  # under
            if x1 + 1 < n and x2 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                a3 = backtrack(x1 + 1, y1, x2 + 1, y2, cnt + 1, "세로", board)
            if x1 + 1 < n and x2 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                a4 = backtrack(x1,y1,)
            a3 = backtrack()  # behind to under
            a4 = backtrack()  # front to under
        else:
            return min(a1, a2, a3, a4, a5, a6)

    else:
        if not arrived:
            if board[x][y + 1] != 1:
                a1 = backtrack(x, )  # right
            a2 = backtrack()  # under
            a3 = backtrack()  # behind to under
            a4 = backtrack()  # front to under
        else:
            return min(a1, a2, a3, a4, a5, a6)


def solution(board):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    # while not arrived(x, y, n):
    answer = backtrack(x1, y1, x2, y2, 0, "가로", board)

    return answer


# dfs 문제

if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    print(solution(board))
