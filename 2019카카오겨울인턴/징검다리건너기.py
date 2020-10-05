def solution(stones, k):

    if len(stones) == 1:
        return stones[0]

    sorted_stones = sorted(stones)

    left = 0
    right = len(sorted_stones) - 1

    while left < right:
        mid = (left + right) // 2
        value = sorted_stones[mid]

        max_consecutive_cnt = 0
        consecutive_cnt = 0
        for stone in stones:
            if stone <= value:
                consecutive_cnt += 1
                max_consecutive_cnt = max(max_consecutive_cnt, consecutive_cnt)
            else:
                consecutive_cnt = 0

        if max_consecutive_cnt >= k:
            right = mid

        # elif max_consecutive_cnt == k: # 더 낮은 value 에서 k 가 나올수도 있다
        #     break
        else:
            left = mid + 1



    return sorted_stones[right]


if __name__ == '__main__':
    stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
    # stones, k = [1], 1
    print(solution(stones, k))
