numbers = [3, 30, 34, 5, 9]


def solution(numbers):
    numbers = [str(num) for num in numbers]
    print(numbers)
    numbers = sorted(numbers, key=lambda x: x * 4)

    if numbers[0] == 0: return '0'

    return ''.join(numbers)

print(solution(numbers))