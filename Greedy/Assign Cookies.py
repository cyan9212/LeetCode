class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer=0
        g.sort()
        s.sort(reverse=True)
        for cookie in g:
            while s and s[-1] < cookie:
                s.pop()
            if s:
                answer+=1
                s.pop()
            else:
                break     
        return answer
