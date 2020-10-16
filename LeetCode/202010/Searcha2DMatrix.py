import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        first_vals = [row[0] for row in matrix]
        row_idx = bisect.bisect(first_vals, target)

        if row_idx >= 1:
            row = matrix[row_idx - 1]
        else:
            return False

        idx = bisect.bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    # print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))
    print(s.searchMatrix([[1]], 2))
