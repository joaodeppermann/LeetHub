class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = []
        for r in range(numRows):
            increment = 2*(numRows - 1)
            for i in range(r, len(s), increment):
                res.append(s[i])
                if r > 0 and r < numRows - 1 and i + increment - 2*r < len(s):
                    res.append(s[i + increment - 2*r])
        
        return "".join(res)