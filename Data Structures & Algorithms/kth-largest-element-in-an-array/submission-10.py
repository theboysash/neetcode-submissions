from collections import deque

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we have an array
        #we keep appending to the array while its <= nums
        #when its bigger than k, we pop
        #we return the last element in the arrau
        heap = []
        for num in nums:
            
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        x = heapq.heappop(heap)
        return x
      