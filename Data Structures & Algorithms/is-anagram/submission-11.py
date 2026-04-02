class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # input is 2 strings, output is bookean
        #instead of returning the sorted, we can use ord() and an array to keep track of how many times chars are present

        if len(s) != len(t):
            return False
        
        count = [0]*26
        for i in range(len(s)):

            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -= 1 # inputs contain only lower case so dont need to worry about checking cap
        
        for value in count:
            if value != 0:
                return False
        return True 