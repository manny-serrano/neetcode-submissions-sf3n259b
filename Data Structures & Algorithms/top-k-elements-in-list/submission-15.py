class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {}
        freqmap = [[] for i in range(len(nums)+1)]



        for i in nums:
            found[i] = found.get(i, 0) + 1

        for key, value in found.items():
            freqmap[value].append(key)

        output = []
        for i in range(len(freqmap)-1, 0, -1):
            for element in freqmap[i]:
                output.append(element)
                if len(output) == k:
                    return output
       
            
            


            
        
        