class Solution:
    def trap(self, height: List[int]) -> int:
        #input is non negative array integers of length n
        #output is integer which is total empty area between bars

        # water has to be between 2 bars of min height (l,r)


        l, r = 0, len(height) -1
        totalwater = 0

        leftMax = height[l]
        rightMax = height[r]
        while l<r:
            if leftMax <= rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                totalwater += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                totalwater += rightMax - height[r]
        return totalwater


        







        
        