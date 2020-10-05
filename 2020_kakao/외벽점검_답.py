from itertools import permutations


def solution(n, weak, dist):
    # 점 한개가 2개 좌표를 갖는다. 애초부터. 단, 하나만 체크되도 2 좌표 모두 체크된다. => 시계, 반시계 생각할 필요 없음

    answer = len(dist) + 1
    dist.sort(reverse=True)

    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # 친구들 다 투입해보면서, length 만큼 dist 개수 커버되는지 확인


    for i in range(length):  # 시작점을 각각 다르게 해본다. 0번째부터 len(weak)-1번째까지

        possible_permutation = permutations(dist)
        point_to_cover = weak[i:i + length]

        for comb in possible_permutation:
            friend_idx = 0
            st = point_to_cover[0]
            covered_distance = st + comb[friend_idx]
            cnt = 1

            for point in point_to_cover:
                if point > covered_distance:
                    cnt += 1
                    if cnt > len(comb):
                        break
                    else:
                        friend_idx += 1
                        covered_distance = point + comb[friend_idx]

            answer = min(answer, cnt)  # 다 써서 합격되는 경우는 어쩔 것인

    if answer < len(dist) + 1:
        return answer
    else:
        return -1


if __name__ == "__main__":
    # print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
    # print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
    # print(solution(20, [1, 3, 4, 9, 10, 14, 16, 18], [1, 2, 3]))
    # print(solution(20, [0, 7, 8, 10, 17, 18], [7, 2, 1]))

    # print(solution(50, [1, 5, 10, 16, 22, 25], [3, 4, 6]))
    # print(solution(50, [1], [6]))
    print(solution(50, [1, 5, 10, 12, 22, 25], [4, 3, 2, 1]))