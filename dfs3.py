result = []
def dfs(graph, start, end , path = [], visit=[]):
    if start == end:
        result.append(path)
    if not set(graph[start]).difference(set(visit)):
        return
    for n in graph[start]:
        if n not in visit:
            dfs(graph, n, end ,path + [n] , visit+[n])

    return result


graph = {"a":["b","c","d","e"], "b":["a","d"],"c":["a","e"],"d":["a","b"],"e":["a","c"]}

print(dfs(graph, "e","b"))