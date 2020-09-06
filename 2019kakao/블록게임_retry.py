def solution(board):
    n = len(board)
    count = 0

    def column_clean_until_row(r, c):
        for i in range(r):
            if board[i][c] != 0:
                return False
        return True

    def isA(r, c):
        if r + 1 <= n - 1 and c + 2 <= n - 1 and \
                board[r][c] == board[r + 1][c] == board[r + 1][c + 1] == board[r + 1][c + 2]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 1, c + 1) and column_clean_until_row(r + 1,
                                                                                                                c + 2):
                board[r][c] = board[r + 1][c] = board[r + 1][c + 1] = board[r + 1][c + 2] = 0

                return True

    def isB(r, c):
        if r + 2 <= n - 1 and c - 1 >= 0 and \
                board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 2][c - 1]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 2, c - 1):
                board[r][c] = board[r + 1][c] = board[r + 2][c] = board[r + 2][c - 1] = 0
                return True

    def isC(r, c):
        if r + 1 <= n - 1 and c - 2 >= 0 and board[r][c] == board[r + 1][c - 2] == board[r + 1][c - 1] == \
                board[r + 1][c]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 1, c - 1) and column_clean_until_row(r + 1,
                                                                                                                c - 2):
                board[r][c] = board[r + 1][c - 2] = board[r + 1][c - 1] = board[r + 1][c] = 0
                return True

    def isD(r, c):
        if r + 2 <= n - 1 and c + 1 <= n - 1 and board[r][c] == board[r + 1][c] == board[r + 2][c] == \
                board[r + 2][c + 1]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 2, c + 1):
                board[r][c] = board[r + 1][c] = board[r + 2][c] = board[r + 2][c + 1] = 0
                return True

    def isE(r, c):
        if r + 1 <= n - 1 and c - 1 >= 0 and c + 1 <= n - 1 and board[r][c] == board[r + 1][c - 1] == \
                board[r + 1][c] == board[r + 1][c + 1]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 1, c - 1) and column_clean_until_row(r + 1,
                                                                                                                c + 1):
                board[r][c] = board[r + 1][c - 1] = board[r + 1][c] = board[r + 1][c + 1] = 0
                return True

    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:

                if isA(r, c):
                    count += 1
                elif isB(r, c):
                    count += 1
                elif isC(r, c):
                    count += 1
                elif isD(r, c):
                    count += 1
                elif isE(r, c):
                    count += 1
                else:
                    continue

    return count


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 7, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 7, 7, 7, 0, 0, 4, 0, 0, 0],
             [6, 6, 0, 0, 0, 4, 4, 0, 0, 0],
             [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
             [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
             [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]
             ]

    print(solution(board))
