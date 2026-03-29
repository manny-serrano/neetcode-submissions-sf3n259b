class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can create a hashmap to track count for each number

        count = {}
        #count has numbers as the key, their frequency as values
        #freq is list with 
        freq = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = count.get(number, 0) + 1

        for key, value in count.items():
            freq[value].append(key)

        output = []
        for ind in range(len(freq)-1, 0, -1):
            for i in freq[ind]:
                output.append(i)
           
            if len(output) == k:
                return output
        


        
        

            








        

        

            





            


            
