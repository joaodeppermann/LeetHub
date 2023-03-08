class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        maxLen = -inf
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            maxLen = max(maxLen, sum(basket.values()))
        return maxLen if maxLen != -inf else 0
            
                
            