class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for a in nums:
            if nums.count(a) == 1:
                return a 
