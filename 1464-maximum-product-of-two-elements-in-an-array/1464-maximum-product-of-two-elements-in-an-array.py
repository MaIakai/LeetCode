from collections import deque
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        
        
        return: maximum value of (nums[i]-1)*(nums[j]-1)
        """
        
        queue=deque()
        
        maxP=0
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if maxP<(nums[i]-1)*(nums[j]-1):
                    maxP=(nums[i]-1)*(nums[j]-1)
        
        
        return maxP