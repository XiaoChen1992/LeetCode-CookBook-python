class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] in vowels and s[j] in vowels:
                    s[i], s[j] = s[j], s[i]
                    j -= 1
                    i += 1
            else:
                if not s[i] in vowels:
                    i += 1
                if not s[j] in vowels:
                    j -= 1
        
        s = ''.join(s)
        return s


if __name__ == '__main__':
    ans = Solution()
    s = "leetcode"
    print(ans.reverseVowels(s))