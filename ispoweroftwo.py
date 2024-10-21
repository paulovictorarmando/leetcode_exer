class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n%2 != 0 or n <= 0:
            return False
        else:
            i = 1
            while i < n:
                if 2**(i) == n:
                    return True
                if 2**i > n:
                    return False
                i += 1