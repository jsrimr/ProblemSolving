# Greedy & bruteforce ( 숫자가 작음 ) & recursion
def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse=True)

    # dist 큰 친구부터 투입. d 로 남은 remain 최대한 커버칠 수 있는 만큼 커버치고, 남은 remain return

    def backtrack(d, remain):
        best = 0
        for r in remain:  # r이 시작점
            left = sum(1 for x in remain if max(r - d, r - d + n) <= x <= r)
            right = sum(1 for x in remain if (r <= x <= r + d))

            bin = max(left, right)
            if bin == left:
            if max(left, right) > best:
                best = max(left, right)
                best_cover =

        return best_cover

    for d in dist:

    # 왼쪽

    # 오른쪽

    # 모든 외벽 점검할 떄까지 ㄱㄱ

    else:
        return -1

    return answer


if __name__ == "__main__":
    print(solution())
