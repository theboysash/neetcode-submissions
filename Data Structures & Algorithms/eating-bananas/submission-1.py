import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #25 10 23 4
        #6 r 1 , 2 r 2, 1 -> 7, 3 1, 6 = 17
        if piles is None:
            return -1
        

        piles.sort()
        best = piles[-1]
        l, r = 1, max(piles) 
        while l<=r:
            mid = (l+r)//2
            total = 0
            for pile in piles:
                total+= math.ceil(pile / mid)
            if total <= h:
                best = min(best, mid)
                r = mid - 1
            else:
                l = mid + 1
        return best
                



        
        