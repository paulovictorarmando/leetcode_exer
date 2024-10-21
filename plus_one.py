class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = 0
        for n in digits:
            a = a*10 + n
        a += 1
        print(a)
        res = list()
        while a > 0:
            res.append(a % 10)
            a = a//10
        return res[::-1]