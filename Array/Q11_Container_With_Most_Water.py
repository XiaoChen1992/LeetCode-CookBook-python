from curses.ascii import SO
from typing import List

from pygments import highlight


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, start, end = 0, 0, len(height) - 1
        while start < end:
            width = end - start
            highth = 0
            if height[start] < height[end]:
                highth = height[start]
                start += 1
            else:
                highth = height[end]
                end -= 1
            
            tmp_area = width * highth
            if tmp_area > max_area:
                max_area = tmp_area
        return max_area


if __name__ == '__main__':
    ans = Solution()
    test = [1,8,6,2,5,4,8,3,7]
    print(ans.maxArea(test))