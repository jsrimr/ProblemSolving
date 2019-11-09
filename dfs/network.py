from collections import defaultdict
def solution(n, computers):
    count = 0
    graph = defaultdict(list)
    for i, connection in enumerate(computers):
        for j, c in enumerate(connection):
            if c==1:
                graph[i + 1].append(j + 1)

    visit = []
    for start in range(n):
        start+=1
        stack = [start]
        if start not in visit:
            while stack:
                node = stack.pop()
                visit.append(node)
                for other in graph[node]:
                    if other not in visit:
                        stack.append(other)
            count+=1

    return count