from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        info = defaultdict(int)

        path_check = set()
        for n, st, ed in trips:
            info[st] += n
            info[ed] -= n
            path_check.add(st)
            path_check.add(ed)

        path_check = sorted(list(path_check))
        cur_n = 0
        for path in path_check:
            cur_n += info[path]
            if cur_n > capacity:
                return False

        return True


if __name__ == '__main__':
    s = Solution()

    print(s.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=4))
    print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
    print(s.carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3)) #True
    print(s.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))

    print(s.carPooling([[2, 1, 5], [3, 3, 7]], 4))
