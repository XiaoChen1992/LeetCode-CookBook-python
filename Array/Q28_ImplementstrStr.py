from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            # print(i)
            # print(haystack[i])
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle):
                    if needle[j] == haystack[i + j]:
                        j += 1
                    else:
                        break
                return i
        return -1
                        
                        
if __name__  == '__main__':
    haystack = "mississippi"
    needle = "issip"
    ans = Solution()
    print(ans.strStr(haystack, needle))
