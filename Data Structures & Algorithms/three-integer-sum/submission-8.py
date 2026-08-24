class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        [-1,0,1,2,-1,-4]

        #-4 -1 -1 0 1 2
        #-4 -1 2
        #-4 -1 2 
        #-4 0 2
        #-4 1 2
        #-1 -1 2
        #-1 0 1
        res = []
 
        nums.sort()
     
        
        
        for curr in range(0, len(nums)):
            if curr > 0 and nums[curr] == nums[curr-1]:
                    continue
            l = curr+1
            r = len(nums)-1
            while l < r:
                
                if nums[curr]+ nums[l] +nums[r]== 0 :
                    res.append([nums[curr], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]: 
                        l+=1
                    while l < r and nums[r] == nums[r + 1]:
                        r-=1 
                elif nums[curr]+ nums[l] +nums[r]< 0 :
                    l+=1
                else:
                    r-=1
            
        return res