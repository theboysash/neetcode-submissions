class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        nums.sort()
        groups = {}
        
        for num in nums:
           if num in groups:
            groups[num]+=1
           else:
            groups[num]=1
        x=sorted(groups.items(), key=lambda x: x[1], reverse=True)
        for i in range(0,k):
            final.append(x[i][0])
        return final
       

         
        
        
         
        
            

        

        