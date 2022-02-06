from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        # two pointers
        i, j = 1, 0
        start = 0
        ans = []
        while i < len(nums):
            if nums[i] - nums[j] <= 1:  # if two adjacent items' difference is smaller than one, i and j move to next position 
                i += 1
                j += 1
            else:
                if start == j:  # special case for first item 
                    ans.append(str(nums[start]))
                else:
                    ans.append(f'{nums[start]}->{nums[j]}')
                start = i # start to i 
                i += 1   # i and j to next position
                j += 1
        if start == i - 1:  # if left only one item
            ans.append(str(nums[start]))
        else:
            ans.append(f'{nums[start]}->{nums[i-1]}')
        
        return ans
                

if __name__ == '__main__':
    ans = Solution()
    nums = [0,2,3,4,6,8,9]
    print(ans.summaryRanges(nums))