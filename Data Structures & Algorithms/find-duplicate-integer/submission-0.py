class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in range(0, len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
            else:
                return nums[i]
        return -1
       
        