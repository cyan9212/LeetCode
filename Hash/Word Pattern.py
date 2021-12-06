class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        words = s.split()
        if len(pattern)!=len(words): return False
        for p,word in zip(pattern,words):
            if p not in dic:
                dic[p] = word
            else:
                if dic[p]!=word:
                    return False
        if len(set(dic.keys())) != len(set(dic.values())): return False
        return True
