#Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for a in s:
            if a.isalnum():
                res += a
        return res[0:].upper() == res[::-1].upper()
