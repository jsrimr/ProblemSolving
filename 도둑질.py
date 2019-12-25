money = [1,2,3,1]
def solution(money):

    with0 = [money[0], money[1], money[0] + money[2], max(money[0], money[1]) + money[3]]
    wout0 = [money[1], money[2], money[1] + money[3]]
    for m in money[4:]:
        with0.append(max(with0[-2], with0[-3]) + m)
        wout0.append(max(wout0[-2], wout0[-3]) + m)

    return max(with0[-3], with0[-2], wout0[-1])

print(solution(money))