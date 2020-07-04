def maxSubArray(nums) :
    answer = 0
    psum = 0
    for i, el in enumerate(nums):
        #연속합 계속 저장
        psum = max(psum, 0) + el
        answer =  max(answer, psum) # 시작점은 고정이 안되있는데 어떻게 딱 맞을 수 있을까? 끝점은 고정한다 치더라도.

    return answer

if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))