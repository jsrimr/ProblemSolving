def dfs(graph, start, end):

    stack = [[start,[]]]
    visit = []
    path = []
    while stack:
        node, hist = stack.pop()
        # stack.extend(graph[node])
        if node not in visit:
            visit.append(node)
            stack += [[n, hist+[n]] for n in graph[node] if n not in visit]
        if node==end:
            path.append(hist)
    return path


graph = {"a":["b","c","d","e"], "b":["a","d"],"c":["a","e"],"d":["a","b"],"e":["a","c"]}

print(dfs(graph, "e","b"))