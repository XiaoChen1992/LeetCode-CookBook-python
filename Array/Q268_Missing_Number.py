from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Arithmetic sequence
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)