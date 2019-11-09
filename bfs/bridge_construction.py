from collections import defaultdict

def dfs(graph, start, cost_table, visit, n, cost, cur_min = 1000000, prev_prev = None):
    if set(visit) == set(list(range(n))):
        return cost
    prev = start
    for node in graph[start]:
        if node != prev_prev:
            cost = dfs(graph, node, cost_table, visit+[node], n, cost+cost_table[prev][node], cur_min, prev_prev = start)
            if cost< cur_min:
                cur_min = cost

    return cur_min

def solution(n, costs):
    graph = defaultdict(list)
    cost_table = [[0 for _ in range(4)] for _ in range(4)]
    for is1, is2, cost in costs:
        graph[is1].append(is2)
        graph[is2].append(is1)
        cost_table[is1][is2] = cost
        cost_table[is2][is1] = cost

    costs = []
    for start in range(n):
        cost = dfs(graph, start, cost_table, [start], n, 0)
        costs.append(cost)

    return costs

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))