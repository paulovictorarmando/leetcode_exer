class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            i = len(nums) - 1
            while(nums[i] > target):
                i = i // 2
            res = [i for i in range(len(nums)) if nums[i] == target]
            return [res[0], res[-1]]
        return [-1, -1]
