class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #we get the prefixes of left and multiply into res
        #we get suffixes of right and multiply into res

        prefix =  1
        suffix = 1

        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range ( len(nums) - 1 , -1 , -1) :
            res[i] *= suffix
            suffix *= nums[i]
        return res

 

        