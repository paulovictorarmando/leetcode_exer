class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        i = 0
        j = 0
        sig = 1
        for n in s:
            if n not in "0123456789":
                i = i + 1
                if n == '-' or n == '+':
                    if n == '-':
                        sig *= -1
                    break
                else:
                    if n == '\t' or n == ' ':
                        pass
                    else:
                        return 0
            else:
                break
        for n in s:
            if j >= i:  
                if n in "0123456789": 
                    a = a*10 + int(n)
                else:
                    break
            j += 1
        res = a*sig
        if res < (-2)**31:
            return (-2)**31
        elif res > (2**31) - 1:
            return (2**31) - 1
        else:
            return res