result = []
def dfs(graph, start, end , path = [], ):
    if start == end:
        result.append(path)
    if not set(graph[start]).difference(set(path)):
        return
    for n in graph[start]:
        if n not in path:
            dfs(graph, n, end ,path + [n] ,)

    return result


graph = {"a":["b","c","d","e"], "b":["a","d"],"c":["a","e"],"d":["a","b"],"e":["a","c"]}

print(dfs(graph, "e","b"))