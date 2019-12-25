# input : 단어 리스트

# output : 각 단어를 고유하게 해주는 '키' 길이의 합

words = ["word", "war","warrior","world"]
# words = ["go","gone","guild"]

print(solution(words))

def solution(words):
    words = sorted(words)
    forbidden = set()
    storage = dict()  # key : word
    for word in words:
        idx = 1
        while word[:idx] in forbidden:
            forbidden.add(word[:idx])
            idx+=1

        while word[:idx] in storage: #충돌이 일어난 것  key = word[:idx]
            old_key = word[:idx]
            forbidden.add(old_key)
            other_word = storage[old_key]

            if len(word)>idx and len(other_word)>idx :
                del storage[old_key]
                idx += 1
                new_key = other_word[:idx]
                storage[new_key]=other_word

            elif len(word)==idx:
                del storage[old_key]
                idx += 1
                new_key = other_word[:idx]
                storage[new_key]=other_word
                break

            elif len(other_word)==idx:
                idx+=1
                new_key = word[:idx]
                storage[new_key] = word
                break


        storage[word[:idx]] = word

    return sum(map(len, storage.keys()))