class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {x: 0 for x in range(1,len(nums)+1)}
        for num in nums:
            dic[num]+=1
        answer = [0,0]
        for key in dic:
            if dic[key]==2:
                answer[0] = key
            if dic[key]==0:
                answer[1] = key
        return answer
