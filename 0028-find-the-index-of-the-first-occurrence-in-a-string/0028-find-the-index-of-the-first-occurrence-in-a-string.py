class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        def isMatch(n, h):
            initial_n = n
            while n < len(needle) and h < len(haystack):
                if needle[n] == haystack[h]:
                    n += 1
                    h += 1
                else:
                    break
            return n + initial_n == len(needle)
                        
        for i in range(len(haystack)):
            if isMatch(0, i):
                return i
            
        return -1