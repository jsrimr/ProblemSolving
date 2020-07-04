import sys

sys.setrecursionlimit(1000000)


def findEmptyRoom(room_dict, room):
    if room not in room_dict:  # 아직 안 팔린 방 찾았다
        room_dict[room] = (room + 1)  # 다음에 이 방 요구하는 사람은 (이 방 +1) 로 안내해본다
        return room

    else:  # 이미 팔린 방이다.
        next_room = room_dict[room]
        allot = findEmptyRoom(room_dict, next_room)
        room_dict[room] = allot # 다음에 이 방 요구할 사람에게 안내하는 방 업데이트

        return allot


def solution(k, room_number):
    answer = []
    room_dict = {}
    for room in room_number:
        allot = findEmptyRoom(room_dict, room)

        answer.append(allot)

    return answer


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))
