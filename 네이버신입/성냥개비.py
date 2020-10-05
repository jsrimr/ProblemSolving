from itertools import combinations_with_replacement, permutations


def solution(k):
    sticks = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    all_combinations = []
    for i in range(10):
        all_combinations.extend(list(combinations_with_replacement(range(10), i)))

    possible_comb = []
    for comb in all_combinations:
        n_stick_list = [sticks[el] for el in comb]
        if sum(n_stick_list) == k:
            possible_comb.append(comb)

    result = 0
    for comb in possible_comb:
        for tup in set(permutations(comb, len(comb))):  # 0으로 시작하는 거 제거
            if tup[0] != 0:
                result += 1
            if len(tup) == 1 and tup[0] == 0: #0만 예외
                result += 1

    return result


if __name__ == '__main__':
    print(solution(5))
    print(solution(6))
    print(solution(11))
    print(solution(1))
