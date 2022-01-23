from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        # two pointers 
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i] # nums[i] is different with val, we both increase counter and i
                counter += 1
            else:
                continue # wihe nums[i] equals to val, we only increase i. counter is the last index for processed value
        return counter                
        

if __name__ == '__main__':
    test = [0,1,2,2,3,0,4,2]
    ans = Solution()
    print(ans.removeElement(test, val=2))