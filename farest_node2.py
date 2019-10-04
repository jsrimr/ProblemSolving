from collections import defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    distance = [0 for _ in range(n+1)]
    visit = [False for _ in range(n+1)]
    visit[1]= True
    queue = [1]

    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    while queue:

        node = queue.pop(0)
        for other in graph[node]:
            if visit[other] == False:
                visit[other] = True
                # queue.extend(graph[other]) -> 단순 모든 노드 방문
                queue.append(other) # -> 두 노드 사이의 거리 구할 때
                distance[other] = distance[node]+1


    max_distance = max(distance[1:])

    return distance.count(max_distance)


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))