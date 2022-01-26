"""用heapq还是sorted区别不大"""


from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score) == 0:
            return []
        if len(score) == 1:
            return ['Gold Medal']
        
        ans = [None] * len(score)
        tmp_dict = {}
        for idx, item in enumerate(score):
            tmp_dict[item] = idx
            
        counter = 1
        for i in sorted(score, reverse=True):
            if counter == 1:
                ans[tmp_dict[i]] = 'Gold Medal'
            elif counter == 2:
                ans[tmp_dict[i]] = 'Silver Medal'
            elif counter == 3:
                ans[tmp_dict[i]] = 'Bronze Medal'
            else:
                ans[tmp_dict[i]] = str(counter)
            counter += 1
        return ans


if __name__ == '__main__':
    ans = Solution()
    print(ans.findRelativeRanks([10,3,8,9,4]))             