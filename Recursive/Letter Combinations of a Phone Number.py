class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}   
        if len(digits) == 0:
            return []
        stack = []
        for digit in digits:
            stack.append(dic[int(digit)])
        stack = stack[::-1]
        answer = []
        recur('', 0, stack, len(stack),answer)
        return answer
    
def recur(result, cnt, lst, length, answer):
        if len(result) == length:
            answer.append(result)
            return 0
        temp = lst.copy()
        cur = temp.pop()
        for c in cur:
            recur(result+c, cnt+1, temp, length, answer)        
