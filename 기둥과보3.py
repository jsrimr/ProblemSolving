def solution(n, build_frame):
    def check(result):
        for x,y,type_ in result:
            if type_ == 0 :# 기둥
                # 바닥이거나 보가 한쪽 끝에 있거나 다른 기둥이 있거나
                if y==0 or (x-1,y,1) in result or (x,y,1) in result or (x,y-1,0) in result:
                    continue
                else:
                    return False

            else: #보
                # 한쪽끝이 기둥이거나 양쪽 끝이 다른 보
                if ((x,y-1,0) in result) or ((x+1,y-1,0) in result) or ((x-1, y,1) in result and (x+1, y,1) in result):
                    continue
                else:
                    return False
        return True

    result = set()
    for req in build_frame:
        x, y, type_, install = req
        
        if install:
            # 일단 set:result 에 넣는다
            result.add((x,y,type_))
            # result 를 체크해본다. install 해도 되는지
            if not check(result):
                result.remove((x,y,type_))
        else:  # destroy
            # 일단 set:result 에서 뺀다
            result.remove((x,y,type_))
            # result 를 체크해본다. destroy 해도 되는지 -> 어떻게 체크해야 빠짐없이 체크하지 => !!!전수검사!!!
            if not check(result):
                result.add((x,y,type_))

    return sorted(list(map(list,list(result))))


if __name__ == "__main__":
    # map_ = (solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    #       2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    # for r in map_:
    #     print(r)
    # print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    #       2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
          1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
