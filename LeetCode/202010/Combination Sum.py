from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        d = [[]] + [[] for _ in range(target)]  # 길이 : 최소 2에서 501까지

        # d = [{(1,1,1,1), (1,2,3),  ...} , ]
        candidates.sort()
        for t in range(1, len(d)):  # 1부터 n까지
            for c in candidates:
                if c < t:
                    sub_lists = d[t - c]
                    for sub in sub_lists:
                        if c <= sub[0]:
                            d[t].append([c] + sub)
                if c == t:
                    d[t].append([c])

        return d[t]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
