class Solution:
    def mySqrt(self, x: int) -> int:
        """
        param:
            x: non-negative integer
        
        return square root of x, decimal digits are truncated, and only the integer part of result is returned.
        
        """
        
        start=0
        end=x
        ans=0
        while start<=end:
            mid=(start+end) // 2
            
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start=mid+1
                ans=mid
            else:
                end=mid-1
                
        
        return ans
            
            