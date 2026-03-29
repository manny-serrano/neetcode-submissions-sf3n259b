class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        # input is int array length n -> heights[i] is height of ith bar
        #output is int

        #area = length x width -> maximize both l and w or just area in total

        l, r = 0, len(heights)-1

        #pairs where they are max values 

        while l<r:

            area = (r-l)*min(heights[l], heights[r])
            maxarea = max(area, maxarea)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
            
        
        return maxarea



            
            







        

        



        