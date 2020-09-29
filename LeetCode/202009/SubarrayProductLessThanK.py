from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # two pointer 로 : 언제 beg 를 움직이고 언제 end 를 움직일거나.
        # P<k 면 end 를 키우고 P >= k 면 beg 를 키운다. 이 때,  beg 를 키울 때 subarray 개수를 계산해서 더해준다.

        beg, end, N, P, answer = 0, 0, len(nums), 1, 0

        for beg in range(N):
            end = max(beg, end)
            while end < N:
                if P * nums[end] < k:
                    P *= nums[end]
                    end += 1
                else:
                    break

            answer += (end - beg)
            P /= nums[beg]

        return answer


if __name__ == '__main__':
    s = Solution()

    # print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
    # print(s.numSubarrayProductLessThanK([1, 1, 1], 2))
    # print(s.numSubarrayProductLessThanK([1,2,3], 0))
    # print(s.numSubarrayProductLessThanK([1,1,10,1,1], 5))
    print(s.numSubarrayProductLessThanK([5,6,7,2], 5))
