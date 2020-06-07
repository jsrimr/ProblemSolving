from collections import Counter
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        answer_set = set()

        def process(arr):
            dict_ = Counter(arr)
            ret = ""

            for k, v in sorted(dict_.items()):
                ret += f"coin{k}cnt{v}"

            return ret

        def backtrack(amt, comb):

            if amt == 0:
                answer_set.add(process(comb))
                return

            if amt < 0:
                return

            for coin in coins:
                backtrack(amt - coin, comb + [coin])

        backtrack(amount, [])

        return len(answer_set)


if __name__ == "__main__":
    s = Solution()

    amount = 5
    coins = [1, 2, 5]

    print(s.change(amount, coins))
