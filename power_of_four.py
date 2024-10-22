class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 4:
            return True
        elif n%4 != 0 or n < 4:
            return False 
        else:
            i = 2
            while n > i:
                if 4**i == n:
                    return True
                elif 4**i > n:
                    return False
                i += 1 
