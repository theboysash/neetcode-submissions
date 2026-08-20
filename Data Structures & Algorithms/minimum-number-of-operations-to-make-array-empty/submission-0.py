class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        dictionary = {}
        total = 0
        for i in range(0, len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = 1
            else:
                dictionary[nums[i]] += 1

        for key in dictionary:
            count = dictionary[key]

            if count == 1:
                return -1

            if count % 3 == 0:
                total += count // 3
            elif count % 3 == 1:
         
                total += (count // 3 - 1) + 2
            else:  
                total += count // 3 + 1

        return total