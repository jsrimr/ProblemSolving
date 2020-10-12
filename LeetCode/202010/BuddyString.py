class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        tmp = []
        for c1, c2 in zip(A, B):
            if c1 != c2:
                tmp.append((c1, c2))

        if len(tmp) == 2 and tmp[0][0] == tmp[1][1] and tmp[1][0] == tmp[0][1]:
            return True
        else:
            if not tmp and len(set(A)) < len(A):
                return True
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings(A="aaaaaaabc", B="aaaaaaacb"))
    print(s.buddyStrings("ab", "ab"))
    print(s.buddyStrings("aa", "aa"))
    print(s.buddyStrings("abab", "abab"))
    print(s.buddyStrings("abcaa", "abcbb"))
