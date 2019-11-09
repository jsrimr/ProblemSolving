def solution(K, travel):
    n = len(travel)

    memo = [[0 for j in range(K + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        t_walk, v_walk, t_bike, v_bike = travel[i - 1]

        for j in range(K + 1):
            # walk
            walk = memo[i - 1][j - t_walk] + v_walk if j >= t_walk and memo[i - 1][j - t_walk] != -1 else -1
            bike = memo[i - 1][j - t_bike] + v_bike if j >= t_bike and memo[i - 1][j - t_bike] != -1 else -1

            memo[i][j] = max(walk, bike)

    return memo[n][K]