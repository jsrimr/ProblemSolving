class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key):
        self.key = key
        self.data = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            curr_node.data += 1

            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

        curr_node.data = True
    """
    주어진 prefix 로 시작하는 단어들을
    트라이에서 찾아 리스트 형태로 반환합니다.
    """

    def starts_with(self, prefix):
        curr_node = self.head
        result = 0
        # 트라이에서 prefix 를 찾고,
        for char in prefix: #

            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
        # bfs 로 prefix subtrie를 순회하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(curr_node.children.values())

        while queue:
            curr = queue.pop()
            if curr.data:
                result += 1
            queue += list(curr.children.values())

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
