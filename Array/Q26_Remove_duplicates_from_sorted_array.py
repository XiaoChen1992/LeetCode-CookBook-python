from re import A
from typing import List

# Soluation 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # special case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        counter = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                nums[i - counter] = nums[i] # nums[i - counter] 代表上一组重复数字的最后一个index， 这句话的意思是把最后一个重复的数字换成新的
        return len(nums) - counter

    def removeDuplicates_v2(self, nums: List[int]) -> int:
        # two pointers, counter and i. init counter = 0 and i = 1
        # the left part of counter means processed part.
        # special case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        current = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[current]:
                current += 1
                nums[current] = nums[i]
        return current + 1
        

if __name__ == '__main__':
    ans = Solution()
    test = [0,0,1,1,1,2,2,3,3,4]
    # print(ans.removeDuplicates(test))
    print(ans.removeDuplicates_v2(test))
    
        