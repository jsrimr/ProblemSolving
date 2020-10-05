from collections import defaultdict
from itertools import chain
from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        nodes = set(chain(*equations))

        # 1. build directed graph
        graph = defaultdict(list)
        for (n1, n2), v in zip(equations, values):
            graph[n1].append((n2, v))  # n1 이 n2 에 비해 v배 값을 가진다
            graph[n2].append((n1, 1 / v))

        # 2. 클러스터 구분해서, 클러스터 안의 element 들은 대표값에 비해 몇배의 값을 가지는지 저장 : (cluster_n , k)
        weight = {node: (-1, -1) for node in nodes}

        def dfs(node, v, cluster_n):
            weight[node] = (cluster_n, v)
            for (n2, v2) in graph[node]:
                if weight[n2][0] == -1:
                    dfs(n2, v / v2, cluster_n)

        c_n = 0
        for k,val in weight.items():
            if val[0] == -1:  # 아직 방문 x
                dfs(k, 1, c_n)
                c_n += 1

        # 3. 쿼리돌면서 같은 cluster 면 k1 / k2 를 append

        answer = []
        for (n1, n2) in queries:  # q = ["x1", "x5"]
            if n1 in weight and n2 in weight and weight[n1][0] == weight[n2][0]:
                answer.append(weight[n1][1] / weight[n2][1])
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
    #
    # equations = [["a", "b"], ["e", "f"], ["b", "e"]]
    # values = [3.4, 1.4, 2.3]
    # queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
    #
    equations = [["a", "c"], ["b", "e"], ["c", "d"], ["e", "d"]]
    values = [2.0, 3.0, 0.5, 5.0]
    queries = [["a", "b"]]
    print(s.calcEquation(equations, values, queries))

# x y 등 식에 없던 문자에 대해서는 -1
# ab / cd 등의 조합 처
