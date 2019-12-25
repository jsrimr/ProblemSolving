wants = [1,3,4,1,3,1]
rooms = 10

def solution(wants, n):

    room_assign = dict((k,k) for k in range(1, n+1))
    mother_ = dict((k,[k])for k in range(1,n+1))
    available = [True for k in range(n)]


    answer = []
    for room in wants:
        answer.append(assigned)
        available[assigned - 1] = False

        # update room_assign and mother_
        tmp = mother_[assigned]
        mother_[assigned] = []

        other = room
        empty = False
        while not empty:
            empty = available[other]
            other += 1

        mother_[other] += tmp

        for room in tmp:
            room_assign[room] = other

    return answer

print(solution(wants,rooms))
