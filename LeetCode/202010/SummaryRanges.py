from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []

        if not nums:
            return answer

        if len(nums) == 1:
            return [str(nums[0])]

        cur_st, cur_ed, prev = nums[0], nums[0], nums[0]

        for n in nums[1:]:
            if n > prev + 1:
                answer.append([cur_st, cur_ed])
                cur_st = n
            cur_ed, prev = n, n

        answer.append([cur_st, cur_ed])

        return [f"{st}->{ed}" if st != ed else f"{st}" for (st, ed) in answer]


if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
    print(s.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
    print(s.summaryRanges(nums=[]))
    print(s.summaryRanges(nums=[3]))
