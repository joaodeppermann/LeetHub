class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        for c in t:
            if counter_t[c] > counter_s[c]:
                return c
            