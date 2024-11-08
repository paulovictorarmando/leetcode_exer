class Solution:
    def isHappy(self, n: int) -> bool:
        while n >= 7:
            res = 0
            while n > 0:
                res += (n % 10)**2
                n //= 10
            n = res
        return n == 1 
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(1))
