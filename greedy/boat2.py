def solution(people, limit):
    people.sort()
    answer = 0
    i=0
    j = len(people) - 1


    while i<j:

        if people[i] + people[j] <= limit:
            i+=1
            j-=1

        else:
            j-=1


        answer +=1

    ## 2개나 1개 남음 -> 2개가 어떻게 남아? -> 그렇네.. 코드 수정.. 
    if i==j: # 1개 남음
        answer +=1

    return answer

#print(solution([70, 50, 80, 50]	, 100))
#print(solution([50,60,70,80,90,91], 100))
print(solution([40,40,40,], 100)) # 마지막에 1개 남는 경우
print(solution([70, 50, 80]	, 100)) # 마지막에 2개 남는 경우?
