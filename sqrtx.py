class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
            return 0
        if x < 4:
            return 1
        i = 2
        while i*i < x:
            i += 1
        if i*i > x:
            return i-1
        return i
