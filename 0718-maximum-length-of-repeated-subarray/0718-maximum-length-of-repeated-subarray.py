class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ROWS, COLS = len(nums1) + 1, len(nums2) + 1
        dp = [[0]*COLS for _ in range(ROWS)]                
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
        return max(max(row) for row in dp)            
        
        
        
            
                