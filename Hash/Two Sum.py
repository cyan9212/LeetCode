class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        dic = {}
        for i in range(length):   
            if nums[i] in dic:
                return [dic[nums[i]], i]   
            else:
                dic[target - nums[i]] = i
