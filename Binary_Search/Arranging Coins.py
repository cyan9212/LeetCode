import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if(n<2): return n
        result = (math.sqrt(2*n+0.25))-0.5
        return int(result)
