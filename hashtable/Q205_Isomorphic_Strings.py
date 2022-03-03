class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        
        tmp = {}
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp[s[i]] = t[i]
            else:
                if tmp[s[i]] != t[i]:
                    return False
        return True
        