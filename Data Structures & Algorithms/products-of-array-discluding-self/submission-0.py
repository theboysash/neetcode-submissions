class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(0,len(nums)):
            val = 1
            for j in range(0,len(nums)):
                if j != i:
                    val *= nums[j]
            output.append(val)
        return output
        

 

        