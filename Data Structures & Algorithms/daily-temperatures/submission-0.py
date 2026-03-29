class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        tempstack = [] # pair of tempereature and index []pair= [temp, ind]

        for i, temp in enumerate(temperatures):
            while tempstack and temp > tempstack[-1][0]:
                stackT, stackInd = tempstack.pop()
                result[stackInd] = (i-stackInd)
            tempstack.append([temp, i])

        return result
            

            


        