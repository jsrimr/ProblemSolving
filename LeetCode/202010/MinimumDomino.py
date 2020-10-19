from typing import List
import copy

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        origin_A = A[:]
        origin_B = B[:]

        cnt_A = 0  # A를 전부 같게 시도해보자
        A_possible = True
        for i in range(N):
            if i == 0:
                continue
            if A[i] != A[i - 1]:  # 뒤집어서 가능하면 같게 만들어보자. cnt_A +=1 , 안되면 return -1
                if B[i] == A[i - 1]:
                    A[i], B[i] = B[i] , A[i]
                    cnt_A += 1
                else:
                    A_possible = False
                    break

        A = origin_A
        B = origin_B
        cnt_B = 0
        B_possible = True
        for i in range(N):
            if i == 0:
                continue
            if B[i] != B[i - 1]:  # 뒤집어서 가능하면 같게 만들어보자. cnt_A +=1 , 안되면 return -1
                if A[i] == B[i - 1]:
                    A[i], B[i] = B[i], A[i]
                    cnt_B += 1
                else:
                    B_possible = False
                    break

        if A_possible and B_possible:
            return min(cnt_A, cnt_B)
        elif A_possible and not B_possible:
            return cnt_A
        elif not A_possible and B_possible:
            return cnt_B
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]))
    print(s.minDominoRotations( A = [3,5,1,2,3], B = [3,6,3,3,4]))
