class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        for n in nums1:
            if not nums2:
                return res
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return res
