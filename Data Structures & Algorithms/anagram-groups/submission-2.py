class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction1 = defaultdict(list) 
        for i in strs:
            mapped = [0]*26
            #keeps track of what letters are in string

            for c in i:
                mapped[ord(c)-ord('a')] += 1
                #for each character in the string, find its ascii value and remap it from 0-26

            diction1[tuple(mapped)].append(i)
            #append to dictionary, with the ordered word as key, and list as value
        return list(diction1.values())

        



        