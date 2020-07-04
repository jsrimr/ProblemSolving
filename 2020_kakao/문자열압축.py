def solution(s):
    min_ = len(s)
    final = ""

    for i in range(1,len(s)//2 + 1):
        st = 0
        ed = st + i
        root = s[st:ed]
        next_ = s[ed:ed+i]
        parsed = ""
        cnt = 1
        while ed+i <= len(s):

            root = s[st:ed]
            next_ = s[ed:ed+i]

            if root == next_: #반복될때
                cnt += 1
            else: #반복실패할때

                if cnt > 1:
                    parsed += f"{root}{cnt}"
                else:
                    parsed += f"{root}"
                cnt = 1
            
            st += i
            ed = st + i
        

        #### 끝에 남은거를 root를 사용하지 않고 s[st:] 로 처리해준게 깔끔했다!
        #### 예외로 cnt>1 인경우 숫자 덧붙여주고
        if cnt > 1:
            parsed += f"{s[st:]}{cnt}"
        else:
            parsed += s[st:]

        if len(parsed) < min_:
            min_ = len(parsed)
            final = parsed

    return min_

if __name__ == "__main__":
    print(solution("aabbaccc")) #:7,
    print(solution("abcabcabc")) #:4,
    print(solution("ababcdcdababcdcd")) #:9,
    print(solution("abcabcdede")) #:8,
    print(solution("abcabcabcabcdededededede")) #:14,
    print(solution("xababcdcdababcdcd")) #:17,
    # for k,v in dict_.items():
    #     print(solution(k) == v, solution(k), v)