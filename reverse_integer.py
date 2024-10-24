class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2147483648 or x > 2147483647:
            return 0
        s = 1
        n = 0
        if x < 0:
            x *= -1 
            s = -1
        while x > 0:
            n = n*10 + x%10
            x //= 10
        n *= s
        if n < -2147483648 or n > 2147483647:
            return 0
        return n
