def solution(n, p, c):
    # 매출평균 구하기

    # price = [100, 50, 25, 0]
    price = 100
    revenue = 0
    stock = 0

    for i, (prod, consume) in enumerate(zip(p, c)):
        stock += prod
        if stock >= consume:
            revenue += (consume * price)
            stock -= consume
            price = 100
        else:
            price /= 2
            if price < 25:
                return '%.2f' % (revenue / (i+1))

    return '%.2f' % (revenue / n)

    # 요구사항 1. 재고계산
    # 가격 변동
    # 아웃시 전날 주문은 무효, 재고만 쌓임
    # 3회이상시 아웃, 잘 지키면 다시 100원

    return answer


if __name__ == '__main__':
    n, p, c = 6, [5, 4, 7, 2, 0, 6], [4, 6, 4, 9, 2, 3]
    n, p, c = 7, [6, 2, 1, 0, 2, 4, 3], [3, 6, 6, 2, 3, 7, 6]

    print(solution(n, p, c))
