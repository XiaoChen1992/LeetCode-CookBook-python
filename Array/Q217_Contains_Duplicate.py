from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = {}
        for i in nums:
            if i not in tmp:
                tmp[i] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    ans = Solution()
    print(ans.containsDuplicate(nums=nums))
    