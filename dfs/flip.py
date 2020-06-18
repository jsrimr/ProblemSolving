from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 안쪽에 있으면서 o 면 x 로 바뀜. 다만 바깥에 있는  o 랑 연결 되어 있는 경우에는 제외
        # -> 바깥에 있는 o 랑 연결된  o  제외하고서는 다 x 인 board 를 return 한다면
        # -> do not 
        if not board:
            return
        x = len(board)
        y = len(board[0])
        visited = set()
        failed = set()

        def check(ij):
            nonlocal visited, failed

            i,j = ij

            stack = deque([(i,j)])
            local_visited = set()
            
            ended = False

            while stack:
                #위가 ㅇ 이면 stack 에 add. 가장자리에 와서도 o 이면 ended = True
                i, j = stack.pop()
                if (i,j) in local_visited:
                    continue
                else:
                    local_visited.add((i,j))
                if i==0 or i==(x-1) or j==0 or j==(y-1):
                    ended = True

                #위
                if i > 0 and board[i-1][j]=="O":
                    stack.append((i-1,j))

                #왼쪽
                if j > 0 and board[i][j-1]=="O":
                    stack.append((i,j-1))

                #오른쪽
                if j < (y-1) and board[i][j+1]=="O":
                    stack.append((i,j+1))

                #아래
                if i < (x-1) and board[i+1][j]=="O":
                    stack.append((i+1,j))

            if ended:
                visited = visited.union(local_visited)
                return True
            else:
                failed = failed.union(local_visited)
                return False


        for i in range(x):
            for j in range(y):
                if (i,j) in visited:
                    continue

                if (i,j) in failed:
                    board[i][j] = "X"
                    continue

                if board[i][j] == "X":
                    continue

                if board[i][j] =="O": 
                    if not check((i,j)): # O 이지만 뒤집히지 않는 경우 : 바깥쪽에 있을 때 , 바깥쪽에 있는 ㅇ 랑 이어져 있을 때 
                        board[i][j] ="X"

        return board



                    



if __name__ == "__main__":
    s = Solution()
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
    
    print(s.solve(board))