def solution(n, build_frame):
    def is_ok(map_, x_y):
        # x_y 지점 pillar나 bo 를 설치하거나 없앴다. 괜찮은가?
        x, y = x_y

        if map_[y][x][1]:  # xy에 보가 위치해있을때 괜찮은가
            # 양 옆의 보에 의해 받쳐지거나 기둥에 의해 받쳐지면 괜찮은 상태
            if (x > 0 and map_[y][x-1][1] and x < n and map_[y][x+1][1]) or (y < n and map_[y+1][x][0]) or (x < n and y < n and map_[y+1][x+1][0]):
                return True

        if map_[y][x][0]:  # xy에 기둥이 위치해있을때 괜찮은가
            # 다른 기둥에 의해 받쳐지거나 보 에 의해 받쳐지면 괜찮은 상태
            if y == n or (y < n and map_[y+1][x][0]) or (map_[y][x][1]) or (x > 0 and map_[y][x-1][1]):
                return True

        if (not map_[y][x][1]) and (not map_[y][x][0]):  # 보나 기둥이 없어져서 아무것도 없는 상황
            res1,res2,res3,res4 = (True,True,True,True)
            if x > 0:
                res1 = is_ok(map_, (x-1, y))
            if x < n:
                res2 = is_ok(map_, (x+1, y))
            if y > 0:
                res3 = is_ok(map_, (x, y-1))
            if y > 0 and x > 0:
                res4 = is_ok(map_, (x-1, y-1))

            return res1 and res2 and res3 and res4

        return False

    map_ = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]

    for req in build_frame:
        x, y, bo_pillar, install = req
        y = n - y
        if bo_pillar == 0:  # 기둥일 경우
            if install:
                if not map_[y][x][0]:
                    map_[y][x][0] = True
                    if not is_ok(map_, (x, y)):
                        map_[y][x][0] = False
            else:  # destroy
                if map_[y][x][0]:
                    map_[y][x][0] = False
                    if not is_ok(map_, (x, y)):
                        map_[y][x][0] = True

        else:  # 보일 경우
            if install:
                if not map_[y][x][1]:
                    map_[y][x][1] = True
                    if not is_ok(map_, (x, y)):
                        map_[y][x][1] = False
            else:  # destroy
                if map_[y][x][1]:
                    map_[y][x][1] = False
                    if not is_ok(map_, (x, y)):
                        map_[y][x][1] = True

    answer = []
    for y in range(n+1):
        for x in range(n+1):
            p, bo = map_[y][x]
            if p:
                answer.append([x, n-y, 0])
            if bo:
                answer.append([x, n-y, 1])
    return sorted(answer)


if __name__ == "__main__":
    # map_ = (solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    #       2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    # for r in map_:
    #     print(r)
    print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
          2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
          1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
