from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] in range(1,n+1) and nums[i] != (i + 1):
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]  # i+1 번째 숫자
                nums[tmp - 1] = tmp  # nums[i] 번째 숫자

        return ([False if nums[i] != (i + 1) else n for i, n in enumerate(nums)] + [False]).index(False) + 1


if __name__ == '__main__':
    s = Solution()

    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
    # print(s.firstMissingPositive([7, 8, 9, 11, 12]))
    # print(s.firstMissingPositive([3, 4, 2, 5, 1]))
