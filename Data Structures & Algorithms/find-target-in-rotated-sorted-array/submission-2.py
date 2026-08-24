class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we find the sored array, check if hte value is in there, else its in the other side

        lo = 0 
        hi = len(nums) - 1

        while lo<= hi:
            mid = (lo+hi)//2
            if target == nums[mid]:
                return mid 
            if nums[lo] <= nums[mid]:
                if not nums[lo]<=target<=nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid -1

            if nums[mid]<= nums[hi]:
                if not nums[mid] <= target <= nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1
        