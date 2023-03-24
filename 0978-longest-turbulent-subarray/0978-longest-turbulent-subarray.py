class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # For each arr[i]
        # inc: The length of current valid sequence which ends with two increasing numbers
        # dec: The length of current valid sequence which ends with two decreasing numbers
        res = 1
        inc = 1
        dec = 1
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            elif arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            else:
                dec = 1
                inc = 1
            res = max(res, max(inc, dec))
        return res 
        
#         maxLen = 1
#         run = 1
#         if len(arr) == 1:
#             return 1
#         increaseMode = False
#         if arr[1] < arr[0]:
#             increaseMode = True 
#         for i in range(1, len(arr)):
#             if arr[i] > arr[i - 1]:
#                 if increaseMode:
#                     run += 1
#                     increaseMode = False
#                 else:
#                     run = 2
#             elif arr[i] == arr[i - 1]:
#                 run = 1
#                 if i + 1 in range(len(arr)):
#                     if arr[i + 1] > arr[i]:
#                         increaseMode = False
#                     else:
#                         increaseMode = True
#             else:
#                 if not increaseMode:
#                     run += 1
#                     increaseMode = True
#                 else:
#                     run = 2
#             maxLen = max(maxLen, run)
#         return maxLen
                