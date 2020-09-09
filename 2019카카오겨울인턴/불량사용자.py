import itertools
import re


def solution(user_id, banned_id):
    possible_combination = set()

    candidates_per_ban_id = []
    for ban_id in banned_id:
        candidates_per_ban_id.append(re.findall(ban_id.replace("*", ".{1}"), "\n".join(user_id)))

    for combination in itertools.product(*candidates_per_ban_id):
        comb_set = set(combination)
        if len(comb_set) == len(banned_id):
            possible_combination.add(tuple(comb_set))

    return len(possible_combination)


if __name__ == '__main__':
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]

    user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    print(solution(user_id, banned_id))
