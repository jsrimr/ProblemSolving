from itertools import chain
from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]

        def union_parent(parent, kx_parent, a, b, v):  # a / b = v
            p_a = find_parent(parent, a)
            p_b = find_parent(parent, b)
            if p_a < p_b:
                parent[b] = p_a
                kx_parent[b] = kx_parent[a] / v
            else:
                parent[a] = p_b
                kx_parent[a] = kx_parent[b] * v

        nodes = set(chain(*equations))
        parent = {x: x for x in nodes}
        kx_parent = {x: 1 for x in nodes}  # [1 for _ in range(len(nodes))]

        for (n1, n2), v in zip(equations, values):
            union_parent(parent, kx_parent, n1, n2, v)

        answer = []
        for q in queries:  # q = ["x1", "x5"]
            if q[0] in parent and q[1] in parent and find_parent(parent, q[0]) == find_parent(parent, q[1]):
                answer.append(kx_parent[q[0]] / kx_parent[q[1]])
            else:
                answer.append(-1.0)

        return answer


if __name__ == '__main__':
    s = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"], ["x6", "x7"], ["x7", "x8"]]
    values = [3.0, 4.0, 5.0, 6.0, 1.5, 5.0]
    queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"], ["x6", "x8"]]

    # equations = [["ab", "bc"]]
    # values = [3.0]
    # queries = [["a", "c"]]

    equations = [["a", "b"], ["e", "f"], ["b", "e"]]
    values = [3.4, 1.4, 2.3]
    queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
    print(s.calcEquation(equations, values, queries))

# x y 등 식에 없던 문자에 대해서는 -1
# ab / cd 등의 조합 처
