from collections import deque

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #5 3 7 2 8 9 12 15 4 2 16 - k = 4
        #5
        #3 5 
        #3 5 7
        #2 3 5 7
        #3 5 7   2
        #3 5 7 8
        #5 7 8 9   3
        #7 8 9   5
        #7 8 9 12
        #8 9 12   7
        #8 9 12 15
        #4 8 9 12
        #8 9 12   4
        #8 9 12 16
        #8


        heap = []
  
        for i in range(0 , len(nums)):
            heapq.heappush(heap, nums[i])
            
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]




        


       