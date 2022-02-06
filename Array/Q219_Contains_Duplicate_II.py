from typing import List
from collections import defaultdict


class Solution:
    """Remember to use defaultdict"""
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        
        vals = defaultdict(list)
        for i, num in enumerate(nums):
            vals[num].append(i)
            for idx in vals[num]:
                # iterate each element, if current ont != i, then get |i - idx|
                if idx != i and abs(i - idx)  <= k:
                    return True
        return False
            

if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    ans = Solution()
    print(ans.containsNearbyDuplicate(nums, 1))