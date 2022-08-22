class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        heights: current order that the students are standing in.
        
        expected: non-decreasing order 
        
        return: number of indices where heights[i] != expected[i]
        """
        
        expected=heights.copy()
        
        expected=self.quick_sort(expected)
        
        answer=0
        print(heights)
        print(expected)
        for idx, val in enumerate(heights):
            if heights[idx] != expected[idx]:
                answer+=1
        return answer
    
    def quick_sort(self, lst):
        if len(lst)<=1:
            return lst
        pivot, tail = lst[0], lst[1:]
        
        left=[x for x in tail if x<=pivot]
        right=[x for x in tail if x > pivot]
        
        return self.quick_sort(left) + [pivot] + self.quick_sort(right) 
        
            
            