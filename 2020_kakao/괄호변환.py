def is_balanced(charset):
    return charset.count('(') == charset.count(')')

def is_valid(charset):
    accum = 0
    for c in charset:
        if c == '(':
            accum += 1
        if c == ')':
            accum -= 1
        if accum < 0:
            return False
    if accum == 0:
        return True
    else:
        return False


def split(charset):
    ret = ""
    accum = 0
    for i, c in enumerate(charset):
        if c == '(':
            accum += 1
            ret += c
        if c == ')':
            accum -= 1
            ret += c
        if accum == 0:
            return ret, charset[i + 1:]


def control(charset):  # valid 하게 만듦
    """
    1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. -> 이걸 어떻게 하지? -> 그냥 ( 개수와 ) 같아질 떄까지 만 나누면 됨. 나머지는 v로 떠넘김
 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. -> v 를 먼저하네?!
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
    :param charset:
    :return:
    """
    if charset == "":  # 1
        return ""

    u, v = split(charset)  # 2

    if is_valid(u):  # 3
        v = control(v)
        return u + v

    else:
        tmp = "("
        tmp += control(v)
        tmp += ")"
        u = u[1:-1]
        new_u = ""
        for c in u:
            if c == "(":
                new_u += ")"
            elif c == ")":
                new_u += "("
            else:
                new_u += c
        tmp += new_u
        return tmp


def solution(p):
    return control(p)


if __name__ == '__main__':
    p = "(()())()"
    p = ")("
    p = "()))((()"
    print(solution(p))
