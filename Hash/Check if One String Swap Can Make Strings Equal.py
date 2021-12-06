class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length!=len(s2): return False
        if s1==s2: return True
        diff = 0
        dic1 = {}
        dic2 = {}
        
        for i in range(length):
            if s1[i]!=s2[i]:
                diff+=1
                if diff==3:
                    return False
                dic1[i] = s1[i]
                dic2[i] = s2[i]
        
        if sorted(dic1.values()) == sorted(dic2.values()): return True
        return False
