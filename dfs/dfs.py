def dfs(graph, start, end):

    stack = [start]
    visit = []
    path = []
    while stack:
        node = stack.pop()
        stack.extend(graph[node])
        if node not in visit:
            visit.append(node)
        if node==end:
            path.append(visit)
    return path


graph = {"a":["b","c","d","e"], "b":["a","d"],"c":["a","e"],"d":["a","b"],"e":["a","c"]}

print(dfs(graph, "e","b"))