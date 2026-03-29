class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # can track with pointers, check dist from pointers to return len
        
        l, maxlen = 0, 0 
        found = set()
        for r in range(0, len(s)):
            while s[r] in found:
                found.remove(s[l])
                
                l+=1
            found.add(s[r])
            maxlen = max(maxlen, r - l + 1)
            
        return maxlen



            

            


            






        