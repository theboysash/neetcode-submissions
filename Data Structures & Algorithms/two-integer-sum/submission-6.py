class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            if compliment in comp:
                return [comp[compliment], i]
            comp[nums[i]] = i 
        
        