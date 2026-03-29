class Solution:
    def isPalindrome(self, s: str) -> bool:
        newword = ""
        for i in s:
            if i.isalnum():
                newword+=i.lower()

        return newword == newword[::-1]

        