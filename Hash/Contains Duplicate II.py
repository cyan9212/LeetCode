from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length == 1: return False
        dic = defaultdict(list)
        for i in range(length):
            if dic[nums[i]] and i - dic[nums[i]][-1] <= k:
                return True
            dic[nums[i]].append(i)  
        return False
