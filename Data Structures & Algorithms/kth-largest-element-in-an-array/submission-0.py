class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = nums[len(nums)-k]
        return x
        