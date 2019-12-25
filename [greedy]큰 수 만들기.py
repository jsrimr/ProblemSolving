number = "4177252841"
k = 4

def solution(number, k):
    collection = []

    for num in number:
        while len(collection) > 0 and num > collection[-1] and k > 0:
            collection.pop()
            k-=1
        collection.append(num)

    #원래부터 내림차순인 경우 처리
    if k>0:
        collection = collection[:-k]
    return ''.join(collection)

print(solution(number,k))

