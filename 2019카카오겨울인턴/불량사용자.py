import itertools

def solution(user_id, banned_id):

    candidates_per_ban_id = []
    for ban_id in banned_id:
        tmp = []
        for u_id in user_id:
            if len(ban_id) != len(u_id):
                continue
            else:
                if all([ban_id[i] == u_id[i] if ban_id[i] != "*" else True for i in range(len(ban_id))]):
                    tmp.append(u_id)
        candidates_per_ban_id.append(tmp)
        # candidates_per_ban_id.append(re.findall(ban_id.replace("*", ".{1}"), "\n".join(user_id) + "\n"))

    possible_combination = set()
    for combination in itertools.product(*candidates_per_ban_id):
        comb_set = set(sorted(combination))
        if len(comb_set) == len(banned_id):
            possible_combination.add(tuple(comb_set))

    return len(possible_combination)


if __name__ == '__main__':
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(solution(user_id, banned_id))

    user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    print(solution(user_id, banned_id))

    user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))
