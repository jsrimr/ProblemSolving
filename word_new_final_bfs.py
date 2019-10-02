

def bfs(graph, start, end ):
    queue = [(start, [start])]
    visit = []

    while queue:
        node, hist = queue.pop(0)

        if node == end:
            return hist

        if node not in visit:
            visit.append(node)
            queue += [(n, hist+ [n]) for n in graph[node] if n not in visit]
    return 0


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
    candidates = [word for word in words if len(set(word).difference(set(begin)))==1]
    for begin in candidates:
        path = bfs(graph, begin, target, )
        print(path)
    return len(path)


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
