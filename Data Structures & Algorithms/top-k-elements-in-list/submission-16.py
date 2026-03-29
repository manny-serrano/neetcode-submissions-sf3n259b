class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        foundfreq = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            foundfreq[i] = foundfreq.get(i, 0) + 1
        
        for key,value in foundfreq.items():
            freq[value].append(key)

        output = []
        for i in range(len(freq)-1, 0, -1):

            for element in freq[i]:
                output.append(element)
                if len(output) == k:
                    return output


            
        


        