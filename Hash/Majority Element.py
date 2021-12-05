from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num]+=1
        answer = (0,0)
        for key in dic:
            if dic[key] > answer[1]:
                answer = (key,dic[key])
        return answer[0]
