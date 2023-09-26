class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # counter_s = Counter(s)
        # counter_t = Counter(t)
        # for c in t:
        #     if counter_t[c] > counter_s[c]:
        #         return c
        sum_t = sum_s = 0
        for c in t:
            sum_t += ord(c)
        for c in s:
            sum_s += ord(c)
        return chr(sum_t - sum_s)