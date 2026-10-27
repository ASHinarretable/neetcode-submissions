class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        relativePosition = [0] * len(temperatures)
        stack = [] #store index and temp values

        for i,t in enumerate(temperatures):
            #write the finish/stopping condition
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                relativePosition[stackInd] = (i - stackInd) 
            stack.append([t,i])

        return relativePosition            
