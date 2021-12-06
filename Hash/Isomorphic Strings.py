from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = defaultdict(str)
        for word1,word2 in zip(s,t):
            dic[word1] = word2
        dic = {dic[key]:key for key in dic}
        temp = ''
        for word in t:
            try:
                temp+=dic[word]
            except:
                return False
        if temp == s: return True
        return False
