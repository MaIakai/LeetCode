from heapq import heappush, heappop
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        
        
        return: maximum value of (nums[i]-1)*(nums[j]-1)
        """        
        heap=[]
        
        
        for num in nums:
            heappush(heap,(-num,num))
        
        
        
        return (heappop(heap)[1]-1)*(heappop(heap)[1]-1)