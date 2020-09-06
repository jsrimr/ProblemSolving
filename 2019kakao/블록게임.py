def solution(board):
    r_n, c_n = len(board), len(board[0])
    count = 0

    def column_clean_until_row(r, c):
        for i in range(r):
            if board[i][c] != 0:
                return False
        return True

    def removable_block(r, c):
        if r + 1 <= r_n - 1 and c + 2 <= c_n - 1 and board[r][c] == board[r + 1][c] == board[r + 1][c + 1] == \
                board[r + 1][c + 2]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 1, c + 1) and column_clean_until_row(r + 1,
                                                                                                                c + 2):
                board[r][c] = board[r + 1][c] = board[r + 1][c + 1] = board[r + 1][c + 2] = 0

                return True
        elif r + 2 <= r_n - 1 and c - 1 >= 0 and board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 2][
            c - 1]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 2, c - 1):
                board[r][c] = board[r + 1][c] = board[r + 2][c] = board[r + 2][c - 1] = 0
                return True
        elif r + 1 <= r_n - 1 and c - 2 >= 0 and board[r][c] == board[r + 1][c - 2] == board[r + 1][c - 1] == \
                board[r + 1][c]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 1, c - 1) and column_clean_until_row(r + 1,
                                                                                                                c - 2):
                board[r][c] = board[r + 1][c - 2] = board[r + 1][c - 1] = board[r + 1][c] = 0
                return True
        elif r + 2 <= r_n - 1 and c + 1 <= c_n - 1 and board[r][c] == board[r + 1][c] == board[r + 2][c] == \
                board[r + 2][c + 1]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 2, c + 1):
                board[r][c] = board[r + 1][c] = board[r + 2][c] = board[r + 2][c + 1] = 0
                return True
        elif r + 1 <= r_n - 1 and c - 1 >= 0 and c + 1 <= c_n - 1 and board[r][c] == board[r + 1][c - 1] == \
                board[r + 1][c] == board[r + 1][c + 1]:
            if column_clean_until_row(r, c) and column_clean_until_row(r + 1, c - 1) and column_clean_until_row(r + 1,
                                                                                                                c + 1):
                board[r][c] = board[r + 1][c - 1] = board[r + 1][c] = board[r + 1][c + 1] = 0
                return True
        else:
            return False

        return False

    def check():
        nonlocal count, board
        for r in range(r_n):
            for c in range(c_n):
                if board[r][c] != 0:

                    if removable_block(r, c):
                        count += 1
                        return True
        else:
            return False

    flag = True
    while flag:
        flag = check()

    return count


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
             [7, 7, 7, 0, 0, 0, 4, 0, 0, 0],
             [0, 6, 0, 0, 0, 4, 4, 0, 0, 0],
             [0, 6, 0, 0, 3, 0, 4, 0, 0, 0],
             [6, 6, 0, 2, 3, 0, 0, 0, 5, 5],
             [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]
             ]

    print(solution(board))
