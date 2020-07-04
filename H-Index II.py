from typing import List
class Solution:
    # A scientist has index h if h of his/her N papers have at least h citations each, 
    # and the other N − h papers have no more than h citations each."
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        if citations == []:
            return 0
        def bSearch(arr):
            left = 0
            right = len(arr)
            while left <= right:
                h = (left + right) // 2
                # h가 2일 때 2 of his paper have at least 2 citations each, other 4 papaers have no more than 2 -> left = mid + 1 뒷부분 불만족이므로 left 를 높여준다

                # h가 4일 때 4 of his paper have at least 4 citations each -> x 앞부분 불만족이므로 right 를 낮춰준다 right = mid-1 -> h를 낮게 실험
                if  arr[-h] >= h and arr[N-h-1] > h :# 첫번째 조건 통과하지만 두 번째는 실패
                    left = h + 1
                elif arr[-h] < h and arr[N-h-1] <= h :
                    right = h - 1 
                else:
                    break
            return h

        return bSearch(citations)

if __name__ == "__main__":
    s = Solution()
    citations = [0,1,3,5,6]
    citations = [100]
    print(s.hIndex(citations))
    