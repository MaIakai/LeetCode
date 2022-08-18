class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        answer=dict(zip(nums,nums))
        
        if len(nums)==len(answer.keys()):
            return False
        else:
            return True
        