import heapq

def solution(n, works):
    heap = []

    for work in works:
        heapq.heappush(heap, (-work,work)) # (우선순위, 값)

    for i in range(n):
        w = heapq.heappop(heap)[1]
        if w>0:
            w-=1
        heapq.heappush(heap, (-w, w))

    answer = sum(list(map(lambda x:x[1]**2, heap)))
    return answer

print(solution(4,[4,3,3]))
