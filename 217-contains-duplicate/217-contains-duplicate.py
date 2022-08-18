class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        answer={}
        
        for idx, val in enumerate(nums):
            answer[val]=idx
        
        if len(nums)==len(answer.keys()):
            return False
        else:
            return True
        