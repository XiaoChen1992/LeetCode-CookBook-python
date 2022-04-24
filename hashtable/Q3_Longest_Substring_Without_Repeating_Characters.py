class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        l = 0
        res = 0
        
        for i in range(len(s)):
            while s[i] in sSet:
                sSet.remove(s[l])
                l += 1
            sSet.add(s[i])
            res = max(res, i - l + 1)
        return res


if __name__ == '__main__':
    ans = Solution()
    print(ans.lengthOfLongestSubstring('abcabcdac'))