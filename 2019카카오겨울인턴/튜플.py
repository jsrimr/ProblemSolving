def solution(s):
    answer = []
    aux_set = set()
    # s를 {} 리스트로 만들고 len 별로 정렬하기
    s = s.replace("{", "[").replace("}", "]")
    s = eval(s)
    s.sort(key=lambda x: len(x))

    # 원소 하나씩 answer 에 넣고 list 로 만들어 반환
    for sub_list in s:
        for el in sub_list:
            if el not in aux_set:
                aux_set.add(el)
                answer.append(el)

    return answer

# 짧은거 부터 점점 add해나가기

if __name__ == '__main__':
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))