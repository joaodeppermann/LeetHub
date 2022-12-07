class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        # The previous and current column starts with all 0's and like 
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # traverse the matrix starting from the bootom right 
        # start at len(text1) - 1 because we need to keep the zero at index len(text)
        for y in range(len(text2) - 1, -1, -1):
            for x in range(len(text1) - 1, -1, -1):
                if text2[y] == text1[x]:
                    dp[y][x] = 1 + dp[y + 1][x + 1]
                else:
                    dp[y][x] = max(dp[y + 1][x], dp[y][x + 1])
        return dp[0][0]