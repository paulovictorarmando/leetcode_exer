#median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2] + nums1[(len(nums1)//2) - 1]) / 2
        return nums1[(len(nums1)//2)]
"""
if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))
"""
