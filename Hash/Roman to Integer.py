class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'N':0}
        answer = 0
        temp = 0
        for number in s:
            if temp < dic[number]:
                answer-=temp
            else:
                answer+=temp
            temp = dic[number]
        answer+=temp
        return answer
