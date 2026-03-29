class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        trackfrequency = {}

        for i in nums:
            if i in trackfrequency:
                trackfrequency[i] += 1
            else:
                trackfrequency[i] = 1
        sorteddict = dict(sorted(trackfrequency.items(), key=lambda item: item[1], reverse=True)) 
        ordered = [] 
        output = []  
        for key in sorteddict:
            ordered.append(key)  

        for number in range(k):
            output.append(ordered[number])
        return output
           


        




        