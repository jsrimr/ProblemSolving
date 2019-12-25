import bisect
wants = [1,3,4,1,3,1]
rooms = 10

def solution(wants, n):
    available = list(range(1, n + 1))
    answer = []
    for want in wants:
        #빈 방 binary search 해서 배정
        assign_idx = bisect.bisect_left(available, want)
        answer.append(available[assign_idx])
        #배정하고 난 뒤 방 리스트 변경
        available = available[:assign_idx]+available[assign_idx+1:]

    return answer

print(solution(wants,rooms))