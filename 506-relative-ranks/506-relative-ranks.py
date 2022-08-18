import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        param:
            score: an integer array, score[i] is the score of the ith athlete
            
            all the scores are guranteed to be unique
            
        return: return an array answer of size n where answer[i] is the rank of the ith athlete. 
        """
        result={}
        heap=[]
        for s in score:
            heapq.heappush(heap,(-s,s))
        if len(score)>=1:
            result[heapq.heappop(heap)[1]]="Gold Medal"
            if len(score)>=2:
                result[heapq.heappop(heap)[1]]="Silver Medal"
                if len(score)>=3:   
                    result[heapq.heappop(heap)[1]]="Bronze Medal"
        
        rank=4
   
        while len(heap)>0:
            
            result[heapq.heappop(heap)[1]]=str(rank)
            rank+=1
        
        answer=[]
        for s in score:
            answer.append(result[s])
        return answer
            
        
        