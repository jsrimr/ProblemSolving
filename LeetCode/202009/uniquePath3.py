from itertools import product
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans, empty_ = 0, 0
        r, c = len(grid), len(grid[0])

        def dfs(cur_r, cur_c, empty):
            nonlocal ans

            if grid[cur_r][cur_c] == 2:
                if empty == 0:
                    ans += 1
                return
            grid[cur_r][cur_c] = -2

            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in direction:
                if 0 <= cur_r + dr < r and 0 <= cur_c + dc < c and grid[cur_r + dr][cur_c + dc] >= 0:
                    save = grid[cur_r + dr][cur_c + dc]
                    dfs(cur_r + dr, cur_c + dc, empty - 1)
                    grid[cur_r + dr][cur_c + dc] = save

        for i, j in product(range(r), range(c)):
            if grid[i][j] == 0 or grid[i][j] == 2:
                empty_ += 1
            if grid[i][j] == 1:
                st_r, st_c = i, j

        dfs(st_r, st_c, empty_)

        return ans


if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

    s = Solution()
    print(s.uniquePathsIII(grid))
