class Solution:
    def trap(self, height: List[int]) -> int:

        # contraints 1<=n<=10^3 medium 
        # can do two pointers, no brute force
        #o(n) or nlogn
        #greeady, heap, dynamic?


        # input is array, so two pointers, binary search ?
        # since unsorted two pointers is strong

        #ouptut is single int, need maximum area so DP or GRreedy

        l, r = 0, len(height)-1
        leftMaxHeight = height[l]
        rightMaxHeight = height[r]

        totalWater = 0 

        while l<r:
            if leftMaxHeight <= rightMaxHeight:
                l+=1
                leftMaxHeight = max(leftMaxHeight, height[l])
                totalWater += leftMaxHeight - height[l]
            else:
                r-=1
                rightMaxHeight = max(rightMaxHeight, height[r])
                totalWater += rightMaxHeight - height[r]
        return totalWater
        

            




        




        