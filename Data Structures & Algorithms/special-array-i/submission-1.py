class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)-1):
            if nums[i] % 2 == 0 and nums[i+1] % 2 != 0:
                continue
            elif nums[i] % 2 != 0 and nums[i+1] % 2 == 0:
                continue
            else:
                return False
        return True 

        