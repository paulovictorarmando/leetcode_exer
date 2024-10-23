class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 3 or n == 9:
            return True
        elif n < 9 or n % 3 != 0:
            return False
        else:
            i = 3
            while True:
                if 3**i == n:
                    return True
                elif 3**i > n:
                    return False
                else:
                    i += 1
