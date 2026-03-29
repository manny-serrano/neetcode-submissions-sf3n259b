class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Understand: we are given 2 inputs, a list and integer(k)
        # need to return a list, with top k most frequent in nums
        # we know we aim for o(n) so iterate through whole array


        map1 = {}
        for i in nums:
            if i in map1:
                 map1[i] = map1.get(i) + 1

            if i not in map1:
                map1[i] = map1.get(i, 0) + 1

        def freq(key):
            return map1[key]

        sortedkeys = sorted(map1, key=freq, reverse=True)

        return sortedkeys[:k]



            
            
        
       
       
        

            

            
    
    



        



         


        

            
            
        