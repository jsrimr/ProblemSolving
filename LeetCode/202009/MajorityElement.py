from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        thres = len(nums) / 3
        for k,v in c.items():
            if v > thres:
                ans.append(k)

        return ans


class Solution:
    def majorityElement(self, nums):
        count = Counter()
        for num in nums:
            count[num] += 1
            if len(count) == 3:
                for elem, freq in count.items(): count[elem] -= 1

        cands = Counter(num for num in nums if num in count)
        return [num for num in cands if cands[num] > len(nums) / 3]

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([1,1,1,3,3,2,2,2, 4, 4]))