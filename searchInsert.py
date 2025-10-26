class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums) -1] < target:
           return len(nums)
        elif nums[0] > target:
            return 0
        else:
            left, right = 0, len(nums) -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target and nums[mid - 1] < target:
                    return mid
                else :
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
