class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        param:
            nums: an integer array
        return: the third distinct maximum number in the nums, 
                if the third maximum does not exist, return the maximum number
        """
        unique_nums=list(set(nums))
    
        sorted_nums=self.quick_sort(unique_nums)
        
        if len(sorted_nums)>=3:
            return sorted_nums[-3]
        else:
            return sorted_nums[-1]
        
    def quick_sort(self, lst):
        if len(lst)<=1:
            return lst
        
        pivot, tail = lst[0], lst[1:]
        
        left=[x for x in tail if x<=pivot]
        right=[x for x in tail if x>pivot]
        
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)