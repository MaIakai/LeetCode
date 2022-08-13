class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        dp=[]

        for i in range(len(nums)):
            dp.append(nums[i]**2)
        return sorted(dp)
