class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low= 1
        k = high

        def is_feasible(mid):
            h1 = 0
            for pile in piles:
                if pile <= mid:
                    h1+=1
                else:
                    h1 += math.ceil(pile/mid)
            
            return h1<=h
        
        while low<=high:
            mid = (low+high)//2
            
            if is_feasible(mid):
                k = mid
                high = mid-1
            else:
                low = mid+1
        return k
        
        
            



        
        