def solution(nums):
    max_list = [0] * len(nums)
    min_list = [0] * len(nums)
    max_list[0] = nums[0]
    min_list[0] = nums[0]
    for i in range(1,len(nums)):
        max_list[i] = max(max_list[i-1]*nums[i],min_list[i-1]*nums[i],nums[i])
        min_list[i] = min(min_list[i-1]*nums[i],nums[i],max_list[i-1]*nums[i])
    return max(max_list)

if __name__ == "__main__":
    print(solution([2,3,-2,4])) # 6
    print(solution([-2,0,-1])) # 0 
    print(solution([-7,-8,-1,-2,-9,-6])) # 108
    print(solution([2,-5,-2,-4,3])) # 24