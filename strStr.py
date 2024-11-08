#find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        i = 0
        while i < len(haystack):
            while needle not in haystack[ i : i+ len(needle)]:
                i += 1
            if  needle in haystack[i : i + len(needle)]:
                return i
        return -1
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("Hello", "ll"))
