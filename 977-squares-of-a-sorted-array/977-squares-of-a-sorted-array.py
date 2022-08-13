class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        dp=[]
        sqr=0

        for i in range(len(nums)):
            sqr=nums[i]**2
            dp.append(sqr)
        return sorted(dp)
