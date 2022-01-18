from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, item in enumerate(nums):
            another = target - item
            if another not in m:
                m[item] = idx
            else:
                return [m[another], idx]
        return None 
