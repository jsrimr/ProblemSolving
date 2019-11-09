path = []
# memo = {}
def find_path(graph, begin, target, history, ):
    # 종료조건
    if begin == target:
        path.append(history)
        return
    # 새로운 거 없을 때
    stack = graph[begin]
    while stack:
        node = stack.pop()
        if node not in history: #이미 방문한 곳 안가도록 + 전에거로 안돌아가도록 조치
            find_path(graph, node, target, history + [node], )

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
        find_path(graph, begin, target, [begin])
    if path:
        return min(list(map(len, path)))
    else:
        return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
