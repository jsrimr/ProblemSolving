

def composeRanges(nums):

    split = []
    for i,num in enumerate(nums):
        # 연속되지 않는 구간 등장하면 새로운 구간 , 그 이전에는 계속 ㄱㄱ
        if i != len(nums)-1:
            if num+1 != nums[i+1]:
                #stop
                split.append(i)

    answer = []

    start = 0
    for i in split:
        stop = nums[i]
        if start!= stop:
            answer.append("{0}->{1}".format(nums[start] , stop ))

        else:
            answer.append("{0}".format(nums[start]))
        start = i+1

nums = [-1,0,1,2,6,7,9]

print(composeRanges(nums))