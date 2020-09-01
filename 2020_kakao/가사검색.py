class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
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
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string

    """
    주어진 prefix 로 시작하는 단어들을
    트라이에서 찾아 리스트 형태로 반환합니다.
    """

    def starts_with(self, prefix):
        curr_node = self.head
        subtrie = None

        # 트라이에서 prefix 를 찾고,
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char == "?":
                break
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return 0

        # bfs 로 prefix subtrie를 순회하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(zip(subtrie.children.values(), [1] * len(subtrie.children)))  # Node list

        count_question_m = prefix.count("?")
        result = 0
        while queue:
            curr, depth = queue.pop(0)
            if depth > count_question_m:
                break
            if depth == count_question_m and curr.data != None:
                # result.append(curr.data)
                result += 1
            queue += list(zip(curr.children.values(), [depth + 1] * len(curr.children)))

        return result


def solution(words, queries):
    ordered_Trie = Trie()
    reversed_Trie = Trie()

    for word in words:
        ordered_Trie.insert(word)
        reversed_Trie.insert(word[::-1])

    answer = []
    for q in queries:
        if q.startswith("?"):
            value = reversed_Trie.starts_with(q[::-1])
            answer.append(value)
        else:
            value = ordered_Trie.starts_with(q)
            answer.append(value)

    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    print(solution(words, queries))
