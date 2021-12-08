class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for word in s:
            if word!='#':
                stack1.append(word)
            else:
                if stack1:
                    stack1.pop()
        for word in t:
            if word!='#':
                stack2.append(word)
            else:
                if stack2:
                    stack2.pop()
        return stack1 == stack2
