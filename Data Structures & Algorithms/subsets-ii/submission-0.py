class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        final =[]
        def backtrack(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        for sub in res:
            sub.sort()
            if sub not in final:
                final.append(sub)
            else:
                continue
        return final
        