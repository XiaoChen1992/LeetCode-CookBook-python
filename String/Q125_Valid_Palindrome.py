import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s = s.lower()
        s = re.sub(pattern=r'[^A-Za-z0-9]', repl='', string=s)
        return s == s[::-1]

    def isPalindrome_v2(self, s: str) -> bool:
        if len(s) == 1:
            return True
        tmp = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                tmp += i
        return s == s[::-1]