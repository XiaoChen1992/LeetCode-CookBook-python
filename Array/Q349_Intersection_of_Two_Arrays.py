from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1) == 0) | (len(nums2) == 0):
            return []

        ans = []
        for i in nums1:
            if (i in nums2) and (i not in ans):
                ans.append(i)
        
        return ans
    
    def insersection_v2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1) == 0) | (len(nums2) == 0):
            return []
        else:
            return set(nums1) & set(nums2)