from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        
        ans = []
        for i in words:
            word_to_set = set(i.lower())
            if word_to_set.issubset(first) or word_to_set.issubset(second) or word_to_set.issubset(third):
                ans.append(i)
        return ans                
        