class Solution:
    def numberOfWays(self, s: str) -> int:
        # 010 or 101
        zeros_to_right = s.count("0")
        ones_to_right = s.count("1")
        res = 0
        
        # check for 010
        # each time you hit a one multiply number of zeros to the left and number of zeros to the right
        zeros_to_left = 0
        ones_to_left = 0
        for i in s:
            if i == "0":
                zeros_to_right -= 1
                zeros_to_left += 1
                res += ones_to_left * ones_to_right
            else:
                ones_to_right -= 1
                ones_to_left += 1
                res += zeros_to_left * zeros_to_right
        
        return res
        