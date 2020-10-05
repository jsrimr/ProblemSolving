from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        def check(st):
            cur_gas = gas[st]
            for _ in range(n):

                cur_gas -= cost[st]
                if cur_gas < 0:
                    return False
                st += 1
                if st >= n:
                    st -= n
                cur_gas += gas[st]
            return True

        for st in range(n):
            if check(st):
                return st
        else:
            return -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    s = Solution()
    print(s.canCompleteCircuit(gas, cost))

    print(s.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
