class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for n in range(nums[0], nums[len(nums) - 1]):
            if n not in nums:
                return n
        
        return nums[-1] + 1 if 0 in nums else 0

def main():
    numbers = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    print(s.missingNumber(numbers))

if __name__ == '__main__':
    main()
