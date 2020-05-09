
def maxSubArray(nums) :
    memo = {}
    sub_st = len(nums)

    def calc(idx): # hash 에 값 등록한다.
        nonlocal sub_st

        if len(nums[idx:]) == 1:
            memo[idx] = nums[idx]
            sub_st = idx
            return

        if idx +1 != sub_st: #sub_st 와 idx 가 연속 아니면
            new = nums[idx]
            sub_max = memo[idx+1]

            if new > sub_max: #sub_st 변경
                sub_st
                memo[idx] = new
                
            else:

        
        else: # 연속이면 그대로 new를 더해준다, 포인터 이동



        memo[idx] = max(value, memo[idx+1])

    for i in reversed(range(len(nums))):
        calc(i)

    return memo

if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))