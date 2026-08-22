class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #similar to subsets, except we can reuse element
        #if path = taget-> append path to res 
        #need to track the running total of path 

        res = []
        path = []
        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining - nums[i])
                path.pop()
        backtrack(0, target)
        return res


    