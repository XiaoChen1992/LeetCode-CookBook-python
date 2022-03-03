class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        if needle == haystack or needle == '':
            return 0
        length_needle = len(needle)
        length_haystack = len(haystack)
        for idx_n, item_n in enumerate(needle):
            for idx_h, item_h in enumerate(haystack):
                if item_n ==  item_h:
                    if idx_h + length_needle <= length_haystack:
                        if needle == haystack[idx_h: idx_h + length_needle]:
                            return idx_h
                        else:
                            continue
                    else:
                        return -1
        return -1

    def strStrV2(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        if needle == haystack or needle == '':
            return 0
        h, n = len(haystack), len(needle)
        for i in range(h):
            if haystack[i: i + n] == needle:
                return i
        return -1
        
if __name__ == '__main__':
    a = "hello"
    b = "ll"
    ans = Solution()
    print(ans.strStr(a, b))