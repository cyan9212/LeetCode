class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for word in s:
            if word in '([{':
                stack.append(word)
            else:
                if not stack:
                    return False
                elif stack[-1] not in dic:
                    return False
                elif dic[stack[-1]] != word:
                    return False
                else:
                    stack.pop()
        return not stack
