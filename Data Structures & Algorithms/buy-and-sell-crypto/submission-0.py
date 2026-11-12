class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices) 
        max_profit=0
        l=0
        r=1
        while r<n:
            diff=prices[r]-prices[l]
            if diff>0:
                max_profit = max(max_profit,diff)
            else:
                l=r
            
            r+=1

        
        return max_profit





        


        