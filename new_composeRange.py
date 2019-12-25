def composeRange(nums):
    if not nums:
        return []

    start = stop = nums[0]

    result = []

    for i, num in enumerate(nums):
        stop = num
        # stop : 연속이 끝나면
        if i!=len(nums)-1:
            if num + 1 != nums[i + 1]:
                result.append((start, stop))
                start = stop = nums[i + 1]
    result.append((start,stop))

    answer= []
    for start, stop in result:
        if start != stop:
            answer.append("{0}->{1}".format(start, stop))
        else:
            answer.append("{0}".format(start))
    return answer

# start, stop 둘이 같도록 초기화하고 다음 num으로
# result 에 start,stop 세트 추가

# 다음 num에서 index 안넘치도록 주의
nums = [-1,0,1,2,6,7,9]

print(composeRange(nums))