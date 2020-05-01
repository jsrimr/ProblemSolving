import copy


def solution(stones, k):
    # 주어진 k 에서 몇명까지 건널 수 있을까
    # 최소 1명, 최대 2억명

    # x명이 건널 수 있었다면 x+1 명~ 구간도 시험해보고
    # x명이 건널 수 없었다면 x-1 명~ 구간에서 실험해본다
    min_ = 1
    max_ = 200000000

    while min_ <= max_:
        mid = (min_ + max_) // 2
        tmp = copy.copy(stones)

        for i, stone in enumerate(tmp):
            tmp[i] = stone - mid

        cnt = 0
        for stone in tmp:  # 연속으로 0보다 작은 구간이 k초과하면 아웃. 더 적은 사람을 실험한다
            if stone <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:  # 연속으로 0보다 작은 구간 나옴
                max_ = mid - 1
                break

        else:  # 문제없이 통과했다. 더 많은 사람을 견디는지 시험해보자
            answer = min_
            min_ = mid + 1

    return answer

#
# import copy
#
# INF = 200000000
#
#
# def solution(stones, k):
#     left = 1;
#     right = INF
#
#     while left <= right:
#         mid = (left + right) // 2
#         tmp = copy.deepcopy(stones)
#         for i in range(len(tmp)):
#             tmp[i] -= mid
#
#         cnt = 0
#         check = False
#         for i in range(len(tmp)):
#             if tmp[i] <= 0:
#                 cnt += 1
#             else:
#                 cnt = 0
#
#             if cnt >= k:
#                 check = True
#                 break
#
#         if check is True:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return left

if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
