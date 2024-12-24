class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if  nums2:
            del(nums1[-n:])
            for n in nums2:
                nums1.append(n)
            nums1.sort()
