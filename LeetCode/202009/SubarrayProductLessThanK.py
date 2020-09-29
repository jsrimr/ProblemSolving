from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        N = len(nums)
        answer = 0

        def backtrack(i, k):  # 첫번째 원소는 포함한다고 했을 때
            nonlocal answer
            if k > 1:
                answer += 1
                # for j in range(i + 1, N):
                # print(i)
                if i + 1 < N:
                    backtrack(i + 1, k / nums[i+1])

        for i in range(N):
            backtrack(i, k / nums[i])

        return answer


if __name__ == '__main__':
    s = Solution()

    print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
    print(s.numSubarrayProductLessThanK([1, 1, 1], 2))
