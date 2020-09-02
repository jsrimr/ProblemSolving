class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    트라이에 문자열을 삽입합니다.
    """

    def insert(self, string):
        curr_node = self.head

        for char in string:
            curr_node.data += 1
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.


    """
    주어진 prefix 로 시작하는 단어들을
    트라이에서 찾아 리스트 형태로 반환합니다.
    """

    def starts_with(self, prefix):
        curr_node = self.head

        # 트라이에서 prefix 를 찾고,
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:

            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
        return curr_node.data

def solution(words, queries):

    ordered_Tries = [Trie() for _ in range(10000)]
    reversed_Tries = [Trie() for _ in range(10000)]

    for word in words:
        l = len(word)
        ordered_Tries[l-1].insert(word)
        reversed_Tries[l-1].insert(word[::-1])

    answer = []
    for q in queries:
        l = len(q)
        if q.startswith("?"):
            value = reversed_Tries[l-1].starts_with(q.replace("?","")[::-1])
            answer.append(value)
        else:
            value = ordered_Tries[l-1].starts_with(q.replace("?",""))
            answer.append(value)

    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    print(solution(words, queries))
