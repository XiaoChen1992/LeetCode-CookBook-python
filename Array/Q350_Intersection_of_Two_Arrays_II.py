from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1) == 0) | (len(nums2) == 0):
            return []
        
        counter = {}
        ans = []
        
        for i in nums1:
            counter[i] = counter.get(i, 0) + 1
        
        for i in nums2:
            if i in counter:
                if counter[i] > 0:
                    ans.append(i)
                    counter[i] = counter.get(i) - 1
                    
        return ans
                

if __name__ == '__main__':
    test1 = [1, 1, 2, 2]
    test2 = [2]
    ans = Solution()
    print(ans.intersect(test1, test2))