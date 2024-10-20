class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            a = list()
            while x > 0:
                a.append(x%10)
                x = x // 10
            return (a[:] == a[::-1])
        else:
            return False