path = []


# memo = {}
def find_path(graph, begin, target, history, candidate):
    # 종료조건
    if begin == target:
        path.append(history)
        return
    # 새로운 거 없을 때
    if not candidate:
        return

    for node in candidate:
        new_candidate = candidate.difference(set([node]))
        find_path(graph, node, target, history + [node], new_candidate)

    return path


def solution(begin, target, words):
    graph = {}
    for word in words:
        graph[word] = []
        # memo[word] = [word]
    for word in words:
        if graph.get(word):
            continue
        for other in words:
            if len(set(word).difference(set(other))) == 1 and word != other:
                graph[word].append(other)

    cand = find_path(graph, begin, target, [begin], set(graph[begin]))
    if cand:
        return min(list(map(len, cand)))
    else:
        return 0


print(solution('hot', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
