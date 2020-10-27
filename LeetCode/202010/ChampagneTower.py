class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = query_row + 1
        if n * (n + 1) / 2 <= poured:
            return 1.0
        elif (n - 1) * n / 2 >= poured:
            return 0.0
        else:
            split = [1 if i == 0 or i == (n - 1) else 2 for i in range(n)]
            excess = poured - (n - 1) * n / 2
            return excess * split[query_glass] / sum(split)


if __name__ == '__main__':
    s = Solution()
    # print(s.champagneTower(poured=100000009, query_row=33, query_glass=17))
    # print(s.champagneTower(poured=2, query_row=1, query_glass=1))
    print(s.champagneTower(25, 6, 1))
