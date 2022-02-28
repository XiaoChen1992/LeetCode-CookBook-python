from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for i in nums:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)
        ans = []
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans
    # could also use index to identity positive and negative