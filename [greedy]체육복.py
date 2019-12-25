def solution(n, lost, reserve):
    student = [1 for _ in range(n + 2)]

    for l in lost:
        student[l] -= 1
    for r in reserve:
        student[r] += 1

    saved=0
    for i in range(1, n + 1):
        if student[i - 1] == 0 and student[i] > 1:
            student[i] -= 1
            student[i - 1] += 1
            saved+=1
            print("left")

        elif student[i + 1] == 0 and student[i] > 1:
            student[i] -= 1
            student[i + 1] += 1
            saved += 1
            print("right")

    # return n-len(lost)+saved
    return len([s for s in student[1:-1] if s>0 ])

n=10
lost=[2,4,7,9]
reserve=[3,7,8]
print(solution(n,lost,reserve))