from collections import defaultdict
def bfs(graph, start, end):
    queue = [[start, []]]
    visit = []
    path = []
    while queue:
        node, hist = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue += [[n, hist + [n]] for n in graph[node] if n not in visit]
        if node == end:
            path.append(hist)
    return path

def solution(n, edge):
    graph = defaultdict(list)
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    lengths = []
    for end in set(list(range(1,n+1))):
        if end == 1:
            continue
        else:
            path = bfs(graph, 1, end)
            lengths.append(len(path))

    min_ = min(lengths)
    answer = lengths.count(min_)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))