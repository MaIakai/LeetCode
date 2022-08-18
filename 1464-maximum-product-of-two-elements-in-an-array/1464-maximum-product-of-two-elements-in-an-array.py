import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        
        
        return: maximum value of (nums[i]-1)*(nums[j]-1)
        """        
        heap=[]
        for num in nums:
            heapq.heappush(heap,(-num,num))
        
        first=heapq.heappop(heap)[1] - 1
        second=heapq.heappop(heap)[1] - 1
        
        
        return first * second