result = []
# memo = {}
def dfs(graph, start, end , path = [], ):
    if start == end:
        result.append(path)
    if not set(graph[start]).difference(set(path)):
        return
    for n in graph[start]:
        if n not in path:
            dfs(graph, n, end ,path + [n] ,)

    return result

def solution(begin, target, words):
    graph = {}
    # pair = {}
    for word in words:
        graph[word] = []
        # pair[word] = []
    for word in words:
        if graph.get(word):
            continue
        for other in words:
            if len(set(word).difference(set(other))) == 1 and word != other:
                graph[word].append(other)

    #for word with intersection with begin:
    candidates = [word for word in words if set(word).intersection(set(begin))]
    for begin in candidates:
        dfs(graph, begin, target, [begin])
    if result:
        # print("result:", result)
        return min(list(map(len, result)))
    else:
        return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
