class Solution:
    def countPrimes(self, n: int) -> int:
        """
        param:
            n: an integer
        
        return the number of prime numbers that are less than n
        """
        if n<=2:
            return 0
        primes=[True] * (n+1)
        i=2
        while i*i<n:
            if primes[i]:
                for j in range(i*2, n, i):
                    primes[j]=False
                    j+=1
            i+=1
            
        ans=0
        for i in range(2, n):
            if primes[i]==True:
                ans+=1
            
        
                
        return ans
            
        