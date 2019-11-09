import bisect

def solution(people, limit):
    people_  = sorted(people)
    paired = [0 for _ in range(len(people_))]

    pair = 0
    for i , p in enumerate(people_):
        if paired[i]:
            continue
        flag = False

        j = bisect.bisect(people_, limit - p)

        if j-1> i  and people_[j-1] + people_[i] <= limit and paired[j-1]==0:
            flag = True
        if flag:
            pair += 1
            paired[i] = 1
            paired[j-1] = 1

    # print(pair)
    return len(people_) - pair


print(solution([40,50,60,70,80,90,91], 100))