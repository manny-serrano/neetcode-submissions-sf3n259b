class Solution:

    # want to join list of strings, cant use any symbol only because if it is in the string, when we decode it it is going to think its more words than necessary
    #we can keep track of how many characters are supposed to be in each word

    def encode(self, strs: List[str]) -> str:

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result

        #"4#code5#manny"




        
        
       
    def decode(self, s: str) -> List[str]:
        # i keeps track of index position 
        result, i = [], 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            # append the word to list, and it ends at j+1+length but not including it
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return result






        
    
         
       