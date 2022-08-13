class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        dp=[]
        sum=0
        for i in range(len(gain)):
            dp.append(sum)
            sum+=gain[i]
        dp.append(sum)
        return max(dp)