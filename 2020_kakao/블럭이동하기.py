from collections import deque


class Node:
    def __init__(self, r1, c1, r2, c2, state, cnt):  # cross and long
        self.r1, self.r2, self.c1, self.c2 = r1, r2, c1, c2
        self.state = state
        self.cnt = cnt

    def getXY(self):
        return self.r1, self.c1

    def getXY2(self):
        return self.r2, self.c2


def solution(board):
    start_node = Node(0, 0, 0, 1, "cross", 0)
    queue = deque([start_node])
    visited = set()

    n = len(board)
    while queue:
        node = queue.popleft()
        if (node.getXY(), node.getXY2()) in visited:
            continue
        visited.add((node.getXY(), node.getXY2()))

        r1, c1 = node.getXY()
        r2, c2 = node.getXY2()
        cnt = node.cnt
        print(r1, c1, r2, c2, node.state, cnt)
        if (r1, c1) == (n - 1, n - 1) or (r2, c2) == (n - 1, n - 1):
            break
        # 8가지 *2
        if node.state == "cross":  # 가로
            if c2 + 1 <= n - 1 and board[r2][c2 + 1] == 0:  # right empty -> go to right,
                queue.append(Node(r1, c1 + 1, r2, c2 + 1, "cross", cnt + 1))
            if c1 - 1 >= 0 and board[r1][c1 - 1] == 0:  # left empty -> go to left
                queue.append(Node(r1, c1 - 1, r2, c2 - 1, "cross", cnt + 1))
            if r1 - 1 >= 0 and board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:  # up empty -> go up, rotate*2
                queue.append(Node(r1 - 1, c1, r2 - 1, c2, "cross", cnt + 1))
                queue.append(Node(r2 - 1, c2, r2, c2, "long", cnt + 1))
                queue.append(Node(r2 - 1, c1, r2, c1, "long", cnt + 1))
            if r2 + 1 <= n - 1 and board[r1 + 1][c1] == 0 and board[r2 + 1][
                c2] == 0:  # under empty -> go under, rotate*2
                queue.append(Node(r1 + 1, c1, r2 + 1, c2, "cross", cnt + 1))
                queue.append(Node(r2, c2, r2 + 1, c2, "long", cnt + 1))
                queue.append(Node(r2, c1, r2 + 1, c1, "long", cnt + 1))
        else:  # long

            if c2 + 1 <= n - 1 and board[r1][c1 + 1] == 0 and board[r2][c2 + 1] == 0:  # 오른쪽이 비었을 때 -> 오른쪽으로 이동, 회전 *2
                queue.append(Node(r1, c1 + 1, r2, c2 + 1, "long", cnt + 1))
                queue.append(Node(r2, c2, r2, c2 + 1, "cross", cnt + 1))
                queue.append(Node(r1, c1, r1, c1 + 1, "cross", cnt + 1))
            # 왼쪽이 비었을때 -> 왼쪽으로 이동, 회전 *2
            if c2 - 1 >= 0 and board[r1][c1 - 1] == 0 and board[r2][c2 - 1] == 0:
                queue.append(Node(r1, c1 - 1, r2, c2 - 1, "long", cnt + 1))
                queue.append(Node(r1, c2 - 1, r1, c2, "cross", cnt + 1))
                queue.append(Node(r2, c2 - 1, r2, c2, "cross", cnt + 1))
            # 위쪽이 비었을로 때 -> 위로이동
            if r1 - 1 >= 0 and board[r1 - 1][c1] == 0:
                queue.append(Node(r1 - 1, c1, r2 - 1, c2, "long", cnt + 1))
            # 아래쪽이 비었을 때 -> 아래로 이
            if r2 + 1 <= n - 1 and board[r2 + 1][c1] == 0:
                queue.append(Node(r1 + 1, c1, r2 + 1, c2, "long", cnt + 1))

    return node.cnt


if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
    board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 0]]
    print(solution(board))
