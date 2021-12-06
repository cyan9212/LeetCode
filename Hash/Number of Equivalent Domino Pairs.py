from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        answer = 0
        dic = defaultdict(int)
        for domi in dominoes:
            domi.sort()
            dic[(domi[0], domi[1])]+=1
            
        for key in dic:
            val = dic[key]
            if val!=1:
                temp=0
                while val!=0:
                    val-=1
                    temp+=val
                answer+=temp
        return answer
