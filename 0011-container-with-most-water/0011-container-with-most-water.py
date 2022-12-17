class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = -1
        while l < r:
            curArea = (r - l)*min(height[l], height[r])
            if height[r] >= height[l]:
                l += 1
            else: 
                r -= 1
            maxArea = max(maxArea, curArea)
        return maxArea