from collections import Counter
from itertools import permutations


def solution(n, edges):
    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    candidates = permutations(range(len(edges)), 2)
    for (i1, i2) in candidates:

        tmp_edges = edges[:]
        tmp_edges.remove(edges[i1])
        tmp_edges.remove(edges[i2])

        parent = [x for x in range(n)]

        for (n1, n2) in tmp_edges:
            union_parent(parent, n1, n2)

        c = Counter(parent)
        if len(set(c.values())) == 1:
            return [i1, i2]


# 제거해야 하는 간선 번호를 순서대로 return -> retrun candidate
#  노드 수가 같은 부분 트리 세개로 분리해야함 -> def is_same_number(graph):


if __name__ == '__main__':
    n, edges = 9, [[0, 2], [2, 1], [2, 4], [3, 5], [5, 4], [5, 7], [7, 6], [6, 8]]
    # n, edges = 9, [[0, 2], [2, 1], [3, 5], [5, 4], [7, 6], [6, 8]]
    print(solution(n, edges))
