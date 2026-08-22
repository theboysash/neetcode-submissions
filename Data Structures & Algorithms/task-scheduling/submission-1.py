from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-freq for freq in counter.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time +=1 
            if heap:
                freq = heapq.heappop(heap)+1
                if freq != 0:
                    queue.append((freq, time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time


                
        