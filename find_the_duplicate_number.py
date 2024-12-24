class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            if num in numbers:
                return num
            numbers.add(num)
