class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        cpy = list()
        for n in nums:
            if n not in cpy:
                cpy.append(n)
        for a in cpy:
            nums[i] = a
            i += 1
        return i