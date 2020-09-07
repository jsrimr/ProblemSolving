def solution(food_times, k):
    food_times_with_idx = [(time, i + 1) for i, time in enumerate(food_times)]
    sorted_f_times = sorted(food_times_with_idx)

    jump_time = 0
    n_remain_food = len(sorted_f_times)
    accum_time = 0
    for t, _ in sorted_f_times:
        accum_time += (t-jump_time) * n_remain_food

        if accum_time > k: # 이퀄이면 몇개 오답나옴
            accum_time -= (t-jump_time) * n_remain_food
            break

        jump_time = t
        n_remain_food -= 1

    if n_remain_food <= 0:
        return -1

    candidate = sorted(sorted_f_times[-n_remain_food:], key=lambda x: x[1])
    return candidate[(k - accum_time) % n_remain_food][1]

    # n = len(sorted_f_times)
    # prev = 0 # 기준이 idx 와 time 2개가 아니라 하나로 만들자
    # cnt = 0
    # while True:
    #     idx = prev
    #     t, _ = sorted_f_times[idx]
    #     # while sorted_f_times[idx][0] == t:  # ->  굳이 이렇게 모아서 처리하려 하지 않아도 됨
    #     #     idx += 1
    #
    #     if t * (n-idx) > k: # -> 틀린이유. t 가 아니라 t-jump_time
    #         break
    #     else:
    #         cnt += t * (n-idx)
    #         prev = idx

    # candidate = sorted(sorted_f_times[prev + 1:], key=lambda x: x[1])
    #
    # return candidate[(k - cnt) % len(candidate)][1]


if __name__ == '__main__':
    food_times = [3, 1, 6]
    k = 6
    food_times = [3, 1, 2]
    k = 5
    print(solution(food_times, k))
