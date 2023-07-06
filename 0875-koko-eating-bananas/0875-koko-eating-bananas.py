class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minLimit, maxLimit = 1, max(piles)
        return self.binarySearch(piles, minLimit, maxLimit, h)
        
    def isValidRate(self, piles, rate, limit):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/rate)
        return hours <= limit
    
    def binarySearch(self, piles, minLimit, maxLimit, h):
        left, right = minLimit, maxLimit
        res = -1
        while left <= right:
            mid = left + (right - left) // 2  
            if self.isValidRate(piles, mid, h):
                # store valid rate and try to shrink even more
                res = mid
                right = mid - 1
            else:
                left = mid + 1       
        return res