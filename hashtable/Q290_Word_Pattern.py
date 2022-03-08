class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_len = len(pattern)
        s = s.split(' ')
        s_len = len(s)
        if pattern_len != s_len:
            return False
        
        if len(set(pattern)) != len(set(s)):
            return False
        
        tmp = {}
        
        for i in range(pattern_len):
            if pattern[i] not in tmp:
                tmp[pattern[i]] = s[i]
            else:
                if tmp[pattern[i]] != s[i]:
                    return False
        return True