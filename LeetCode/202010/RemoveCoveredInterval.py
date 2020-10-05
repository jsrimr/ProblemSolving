from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        removed = 0
        max_ed = 0
        for itv in intervals:
            st, ed = itv
            if ed <= max_ed:
                removed += 1
            max_ed = max(max_ed, ed)

        return len(intervals) - removed


if __name__ == '__main__':
    s = Solution()
    print(s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
    print(s.removeCoveredIntervals(intervals=[[1, 4], [2, 3]]))
    print(s.removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]))
    print(s.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
