class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        currL, currR = intervals[0]

        for newL, newR in intervals[1:]:
            if newL <= currR:              # overlap
                currR = max(currR, newR)
            else:                          # no overlap
                result.append([currL, currR])
                currL, currR = newL, newR

        result.append([currL, currR])      # don't forget the last one!
        return result
                

        