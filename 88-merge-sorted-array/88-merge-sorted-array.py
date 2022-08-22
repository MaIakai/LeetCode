class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        param:
            nums1, nums2: non-decreasing order
            m: number of elements in nums1
            n: number of elements in nums2
        
        return: Modify nums1 in-place
        """
        
        nums3=nums1[:m]+nums2
        nums3=self.merge_sort(nums3)
        
        del nums1[:]
        nums1.extend(nums3)
        
    def merge_sort(self, lst):
        if len(lst) < 2:
            return lst
        
        mid=len(lst) // 2
        left=self.merge_sort(lst[:mid])
        right=self.merge_sort(lst[mid:])
        
        merged_lst=[]
        
        l=0
        r=0
        
        while l<len(left) and r < len(right):
            if left[l] < right[r]:
                merged_lst.append(left[l])
                l+=1
            else:
                merged_lst.append(right[r])
                r+=1
        merged_lst += left[l:]
        merged_lst += right[r:]
        
        return merged_lst