import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        param:
            stones: an array of integers (weights)
            
        return: the weight of the last remaining stone, if there are no stones left, return 0
        """
        
        heap=[]
        if not stones:
                return 0
        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        while True:
            
            if len(heap)==1:
                return heapq.heappop(heap)[1]
                
            if len(heap)==0:
                return 0
            y=heapq.heappop(heap)[1]
            x=heapq.heappop(heap)[1]
        
            
            
            
            if x != y:
                heapq.heappush(heap,(-(y-x), y-x))
            

        
        