class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        temp_max=1
        total_max = 1
        nums.sort()
        for  i in range(0,len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                temp_max+=1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                if temp_max > total_max:
                    total_max=temp_max
                temp_max=1
        if temp_max > total_max:
            total_max=temp_max
        return(total_max)