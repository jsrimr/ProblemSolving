from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):

        start, end, N, P, answer = 0, 0, len(nums), 1, 0

        while end < N:
            P *= nums[end]
            while start <= end and P >= k:
                P /= nums[start]
                start += 1

            answer += (end - start + 1)
            end += 1

        return answer


if __name__ == '__main__':
    s = Solution()

    print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
    # print(s.numSubarrayProductLessThanK([1, 1, 1], 2))
    # print(s.numSubarrayProductLessThanK([1,2,3], 0))
    # print(s.numSubarrayProductLessThanK([1,1,10,1,1], 5))
    print(s.numSubarrayProductLessThanK([5, 6, 7, 2], 5))
