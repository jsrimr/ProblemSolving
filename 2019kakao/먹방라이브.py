def solution(food_times, k):
    food_times_with_idx = [(time, i) for i, time in enumerate(food_times)]
    sorted_f_times = sorted(food_times_with_idx)

    n = len(sorted_f_times)
    prev = 0
    cnt = 0
    while True:
        idx = prev
        t, _ = sorted_f_times[idx]
        while sorted_f_times[idx][0] == t:
            idx += 1

        if t * (n-idx) > k:
            break
        else:
            cnt += t * (n-idx)
            prev = idx

    candidate = sorted(sorted_f_times[prev+1:], key=lambda x: x[1])

    return candidate[(k - cnt) % len(candidate)][1]


if __name__ == '__main__':
    food_times = [3, 1, 6]
    k = 6
    # food_times = [3, 1, 2]
    # k = 5
    print(solution(food_times, k))
