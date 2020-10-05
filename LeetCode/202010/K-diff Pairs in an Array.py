from collections import defaultdict
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        answers = set()
        num_and_idx = defaultdict(list)
        for i, n in enumerate(nums):
            num_and_idx[n].append(i)

        for i, n in enumerate(nums):
            for idx in num_and_idx[n+k]:
                if i != idx:
                    answers.add((n, n + k))

        return len(answers)


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3))
    print(s.findPairs([1, 3, 1, 5, 4], 0))
