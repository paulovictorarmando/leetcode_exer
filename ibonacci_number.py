class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
            
def main():
    n = Solution()
    print(n.fib(0))
    print(n.fib(1))
    print(n.fib(2))
    print(n.fib(3))
    print(n.fib(4))
    print(n.fib(5))
if __name__ == "__main__":
    main()
    
