class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()[::-1]
        ans = ''
        for i in range(len(tmp) - 1):
            ans += tmp[i]
            ans += ' '
        ans += tmp[-1]
        return ans
    
    def reverseWrordsV2(self, s: str) -> str:
        return " ".join(s.split()[::-1])