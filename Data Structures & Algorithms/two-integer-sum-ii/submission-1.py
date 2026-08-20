class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        primary = 0
        secondary = 1
        final_1 = -1
        final_2 = -1
        test = []
        #have 2 pointers
        #1 points to our current elements 
        #2 points to the element we are adding 
        #if at some point this combination is greater than the output
        #we restart with the next element bigger than the current one
        while(True):
            if secondary >= len(numbers):
                primary += 1
                secondary = primary + 1
                continue
            if numbers[primary]+numbers[secondary] == target:
                final_1=primary + 1
                final_2=secondary + 1
                break
            elif numbers[primary] + numbers[secondary]< target:
                secondary+=1
            elif numbers[primary]+numbers[secondary]>target:
                primary+=1
                secondary=primary+1
        test.append(final_1)
        test.append(final_2)
        return test