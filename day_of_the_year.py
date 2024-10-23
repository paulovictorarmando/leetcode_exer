class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        m = int(date[5:7]) - 1
        d = int(date[8:])
        y = int(date[0:4])
        while m > 0:
            if m == 2:
                if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                    d += 29
                else:
                    d += 28
            elif m in [4, 6, 9, 11]:
                d+= 30
            else:    
                d += 31
            m -= 1
        return(d)
