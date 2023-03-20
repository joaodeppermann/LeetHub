# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s) + 1) # add + 1 for the base case
#         dp[len(s)] = True # last char after the string is considered as a match... base case
        
#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if (len(w) <= len(s) - i) and s[i : i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break
#         # if the first word found a breaking point compatible 
#         return dp[0]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False