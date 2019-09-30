path = []
# memo = {}
def find_path(graph, begin, target, history, pair, prev):
    # 종료조건
    if begin == target:
        path.append(history)
        return
    # 새로운 거 없을 때
    if graph[begin] == pair[begin]:
        return

    for node in graph[begin]:
        if node not in pair[begin] and node != prev:
            pair[begin].append(node)
            prev = begin
            find_path(graph, node, target, history + [node], pair, prev)

def solution(begin, target, words):
    graph = {}
    pair = {}
    for word in words:
        graph[word] = []
        pair[word] = []
    for word in words:
        if graph.get(word):
            continue
        for other in words:
            if len(set(word).difference(set(other))) == 1 and word != other:
                graph[word].append(other)

    find_path(graph, begin, target, [begin], pair, None)
    if path:
        return min(list(map(len, path)))
    else:
        return 0

print(solution('hot', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
