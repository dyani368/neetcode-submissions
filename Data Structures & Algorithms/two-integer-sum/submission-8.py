class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            comp[remaining] = i
        
        for i in range(len(nums)):
            if nums[i] in comp and comp[nums[i]] != i:
                return [i,comp[nums[i]]]






        
        



        