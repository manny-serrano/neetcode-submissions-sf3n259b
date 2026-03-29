class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)

        stack = []
        for i, value in enumerate(temperatures):
            while stack and value>stack[-1][0]:
                stackValue, stackInd = stack.pop()
                result[stackInd] = (i-stackInd)
            stack.append([value, i]) 
        return result


        