class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLength = 0
        for i in range(len(s)):
            l, r = i, i
            curLength = 1
            
            # odd palidromes
            while l in range(len(s)) and r in range(len(s)) and s[r] == s[l]:
                curLength = r - l + 1
                if curLength > maxLength:
                    res = s[l:r + 1]
                    maxLength  = curLength 
                l -= 1
                r += 1
            
            # even palidromes 
            l, r = i, i + 1
            curLength = 1
            while l in range(len(s)) and r in range(len(s)) and s[r] == s[l]:
                curLength = r - l + 1
                if curLength > maxLength:
                    res = s[l:r + 1]
                    maxLength  = curLength 
                l -= 1
                r += 1
            
        return res