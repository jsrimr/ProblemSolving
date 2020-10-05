def solution(n, weak, dist):
    dist = sorted(dist, reverse=True)

    global_cnt = float("Inf")
    for i in range(len(weak)):
        # tmp_weak = weak[i:] + weak[:i]
        tmp_weak = [0] + [abs(weak[j + 1] - weak[i]) for j in range(len(weak) - 1)]
        # max_tmp_weak = tmp_weak[-1]

        cur_point = -1
        weak_idx = 0
        dist_idx = 0
        while cur_point < tmp_weak[-1]:
            while tmp_weak[weak_idx] <= cur_point:
                weak_idx += 1
            if dist_idx >= len(dist): break
            cur_point = tmp_weak[weak_idx] + dist[dist_idx]
            dist_idx += 1

        global_cnt = min(global_cnt, dist_idx)

    return global_cnt if global_cnt != float("Inf") else -1
    # -1 인 경우도 나타나도록


if __name__ == '__main__':
    n, weak, dist = 12, [1, 5, 6, 10], [1, 2, 3, 4]
    print(solution(n, weak, dist))
