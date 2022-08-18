class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD={}
        tD={}
        for i in s:
            sD[i]=1
        for i in t:
            tD[i]=1

        for i in s:
            if sD[i]:
                sD[i]+=1
        
        for j in t:
            if tD[j]:
                tD[j]+=1
        
        for i in sD.keys():
            if len(s)!=len(t):
                return False
            elif i not in tD.keys():
                return False
            elif i in tD.keys() and sD[i]!=tD[i] :
                return False
            
        
        return True
        