from collections import defaultdict
import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        dic = defaultdict(int)
        nums = re.split('\D',word)
        for num in nums:
            if num!='':
                dic[int(num)]+=1
        return len(dic)
