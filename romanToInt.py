class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        l = len(s)
        res = 0
        while i < l:
            if s[i] == "M":
                res += 1000
            elif s[i] == "D":
                res += 500
            elif s[i] == "C":
                if i + 1 < l and (s[i +1] == 'D' or s[i +1] == 'M'):
                    res -= 100
                else:
                    res += 100
            elif s[i] == "L":
                res += 50
            elif s[i] == "X":
                if i + 1 < l and (s[i +1] == 'L' or s[i +1] == 'C'):
                    res -= 10
                else:
                    res += 10
            elif s[i] == "V":
                res += 5
            else:
                if i + 1 < l and (s[i + 1] == 'V' or s[i +1] == 'X'):
                    res -= 1
                else:
                    res += 1
            i += 1
        return res
