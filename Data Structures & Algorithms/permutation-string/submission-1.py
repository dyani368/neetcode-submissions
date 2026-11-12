class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        from collections import Counter
        freq1 = Counter(s1)
        freq2 = {}

        for r in range(len(s1)):
            if s2[r] in freq2:
                freq2[s2[r]] += 1
            else:
                freq2[s2[r]] = 1
        
        if freq1 == freq2:
            return True
        
        l = 0
        r = len(s1)
        while r<= len(s2)-1:
            if s2[r] in freq2:
                freq2[s2[r]] += 1
            else:
                freq2[s2[r]] = 1

            if r-l+1 > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l+=1

            if freq2 == freq1:
                return True

            r+=1

        return False 
            
        