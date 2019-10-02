path = []
def find_path(graph, begin, target, history, ):
    # 종료조건
    if begin == target:
        path.append(history)
        return
    # 새로운 거 없을 때
    stack = graph[begin]
    while stack:
        node = stack.pop()
        # 이 코드의 문제점 : history 가 그 떄 그때 동적으로 바뀌어야 하는데, e로 시작하면 c쪽 방향은 들리지만 a쪽 방향은 들리지 못하게 된다.
        if node not in history: #이미 방문한 곳 안가도록 + 전에거로 안돌아가도록 조치
            find_path(graph, node, target, history + [node], )


graph = {"a":["b","c","d","e"], "b":["a","d"],"c":["a","e"],"d":["a","b"],"e":["a","c"]}


find_path(graph, "e","b",[])
print(path)