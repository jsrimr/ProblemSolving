def fact_div(n):
    dict_ = {1:1}
    for i in range(2,n):
        dict_[i] = dict_[i-1]*i
    return dict_

def solution(n,k):
    nums = list(range(1,n+1))
    sunsu = []
    div_set = fact_div(n)
    div_ = n-1
    while div_ > 0:
        mok, res = divmod(k, div_set[div_])
        # if div_==1 and res ==0 :
        #     return sunsu + sorted(nums)
        # 나머지 0 아닐 떄
        if res!=0:
            cand = nums[mok]
            nums.remove(cand)
            sunsu.append(cand)
        # 나머지 0 일때
        else:
            cand = nums[mok-1]
            nums.remove(cand)
            sunsu.append(cand)
            # return sunsu + sorted(nums, reverse=True)
        div_ -= 1
        k = res
    return sunsu+nums

# print(solution(5,116))


from itertools import permutations

def solution2(n,k):
    permut = list(permutations(list(range(1,n+1)),n))
    return list(permut[k-1])

n=5
for k in range(1, 120+1):
    if solution(n,k)!=solution2(n,k):
        print(k, solution(n,k), solution2(n,k))