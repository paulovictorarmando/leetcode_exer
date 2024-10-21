class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        while True:
            i += num % 10
            num = num // 10
            if num <= 0:
                if i > 9:
                    num = i
                    i = 0
                else:
                    break
        return i
