class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphanum = ""
        for i in s:
            if i.isalnum():
                alphanum += i.lower()

        
        return alphanum == alphanum[::-1]



        
        


