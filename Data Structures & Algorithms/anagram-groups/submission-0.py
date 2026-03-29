class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Understand: We have input a string array(list of words), we want to return an array with sublists of all anagrams

        #Plan: we can first iterate through list, 2 strings are anagrams if we can sort them and get the same for them
        # each charactef can be from a-z (26)
        # for each string, create array called count that tracks how many of each char in the string
        #create map with the key being the characters and ther frequency and the value being a list of worfs that satisy it
        #overall timecomplexity is o(m*n) where m is number of input stirngs and n is average length of string
        
        map1 = defaultdict(list) # mapping character count of each string to list of anagrams

        
        for i in strs:
            count = [0] * 26 # a - z

            for j in i:
                #ord gets ascii valye of j and welll subtract by "a" to match  a:0, z:25
                count[ord(j) - ord("a")] += 1 # count for each char
            
            map1[tuple(count)].append(i) # want to add/append the string into the count in map
        
        # lists can not be keys, so we will have to make it a tuple since they are immutable

        return map1.values()



        