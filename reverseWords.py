#reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for a in s.split():
            res = a + " " + res
        return res[:-1]
"""
if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
"""
