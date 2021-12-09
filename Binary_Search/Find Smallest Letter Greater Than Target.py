class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = list(set(letters))
        letters.sort()
        left = 0
        right = len(letters)-1
        while left<=right:
            mid = (left+right)//2
            if letters[mid] < target:
                left = mid+1
            elif letters[mid] > target:
                right = mid-1
            else:
                if mid == len(letters)-1:
                    return letters[0]
                else:
                    return letters[mid+1]
        if left>=len(letters):
            return letters[0]
        return letters[left]
