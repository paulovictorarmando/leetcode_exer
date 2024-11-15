class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            while j < len(t):
                if i > len(s)-1:
                    break
                if s[i] == t[j]:
                    i += 1
                j += 1
            break
        return i == len(s)
