from collections import Counter


def solution(N, stages):
    c = Counter(stages)
    accum = {N + 1: c[N + 1] if N+1 in c else 0}
    for i in range(N, 0, -1):
        accum[i] = accum[i + 1] + c[i]

    answer = []
    for i in range(1,N+1):
        fail_rate = c[i] / accum[i] if accum[i] else 0
        answer.append((fail_rate, i))

    answer.sort(key=lambda x: (-x[0], x[1]))

    return [x[1] for x in answer]


if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))

    # 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수


# stage : 1~N
# stages : 사용자별 현재stage [1,2,6,4,6,5,...]
