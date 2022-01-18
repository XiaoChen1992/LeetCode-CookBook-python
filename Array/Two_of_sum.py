from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define a dict
        m = {}
        for idx, item in enumerate(nums):
            another = item - target
            if another not in m:
                m[another] = idx
            else:
                return m[idx]

        return False 
        