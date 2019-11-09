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


graph = {"a": ["b", "c", "d", "e"], "b": ["a", "d"], "c": ["a", "e"], "d": ["a", "b"], "e": ["a", "c"]}

print(bfs(graph, "e", "b"))
