from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_arr = [float('inf') for _ in range(n)]
        for i in range(1, n):
            min_arr[i] = min(nums[i - 1], min_arr[i - 1])

        stack = []
        for i in range(n - 1, 0, -1):
            while stack and stack[-1] < min_arr[i]:
                stack.pop()

            if stack and stack[-1] < nums[i]:
                return True
            # if nums[i] > min_arr[i]:
            stack.append(nums[i])

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.find132pattern([3, 1, 4, 2]))
    print(s.find132pattern([1, 2, 3, 4, ]))
    print(s.find132pattern([-1, 3, 2, 0]))
    print(s.find132pattern([-2, 1, -2]))
