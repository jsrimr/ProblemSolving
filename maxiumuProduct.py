def solution(nums):
    Store = []
    plusStore = []
    minusStore = []
    answer = -float("Inf")

    def arr_product(arr):
        ret = 1
        for el in arr:
            ret *= el
        return ret

    for el in nums:
        # 이전거랑 힘을 합한게 더 크냐, 지금 혼자가는게 더 크냐

        if el > 0: 
            product = arr_product(plusStore) * el

            Store.append(el)
            plusStore.append(el)
            minusStore.append(el)

        elif el < 0: 
            if minusStore:
                product = arr_product(minusStore) * el

                Store.append(el)
                minusStore.append(el)
                plusStore = 

            else:
                product = el

                Store.append(el)
                plusStore = []
                minusStore.append(el)


        else:
            product = 0

            store = []
            plusStore = []
            minusStore = []

        answer = max(answer, product)

        # 0의 존재

    return answer

if __name__ == "__main__":
    print(solution([2,3,-2,4])) # 6
    print(solution([-2,0,-1])) # 0 
    print(solution([-7,-8,-1,-2,-9,-6])) # 108
    print(solution([2,-5,-2,-4,3])) # 24