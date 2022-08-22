class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        param:
            nums: an array of integers which is sorted in ascending order
            target: an integer
        
        return: if target exists, then return its index, else return -1.
        """
        
        start=0
        end=len(nums)-1
        
        while start<=end:
            mid=(end+start) // 2
            
            if nums[mid]==target:
                return mid
            
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        
        return -1
        