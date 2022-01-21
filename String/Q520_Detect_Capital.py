class Solution:
    @classmethod
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if word[0].islower() and word[1].isupper():
                return False
        
        if word[1].isupper():
            result = [word[i].isupper() for i in range(2, len(word))]
        else:
            result = [word[i].islower() for i in range(2, len(word))]
        
        return all(result)
    
    def detectCapitalUse_v2(self, word: str) -> bool:
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word[0].isupper() and word[1:].lower() == word[1:]:
            return True
        else:
            return False

    def detectCapitalUse_v3(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    test = "FlaG"
    print(Solution.detectCapitalUse(test))