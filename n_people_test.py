from itertools import permutations

def solution(n,k):
    permut = list(permutations(list(range(1,n+1)),n))
    return list(permut[k-1])

print(solution(5,67))
