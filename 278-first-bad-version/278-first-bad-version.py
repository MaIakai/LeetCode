# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        param:
            n: versions [1,2, ..., n]
            
        API: isBadVersion(version): returns whether version is bad
        
        """
        
        start=1
        end=n
        
        while start<=end:
            mid=(start+end)//2
            
            if isBadVersion(mid)==True:
                end=mid-1
                ans=mid
            elif isBadVersion(mid)==False:
                start=mid+1
            
        return ans