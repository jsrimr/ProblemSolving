stones = [2,4,5,3,2,1,4,2,5,1]
k = 3

def compute_gap(stones):
    max_gap = 0
    cur = 0
    for st in stones:
        if st != 0:
            cur = 0
            continue
        else:
            cur += 1
            if cur > max_gap:
                max_gap = cur

    return max_gap

def solution(stones, k):
    cnt = 0
    #max_gap 이 k 와 같아지면 return
    while True:
        cnt += 1
        for i, stone in enumerate(stones):
            if stone > 0:
                stones[i] = stone - 1

        max_gap = compute_gap(stones)
        if max_gap == k:
            return cnt

if __name__ == "__main__":
    print("start")
    print(solution(stones,k))