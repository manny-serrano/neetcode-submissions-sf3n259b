class Solution:
    def isPalindrome(self, s: str) -> bool:
        newword = ""
        for i in range(len(s)):
            if s[i].isalnum():
                newword += s[i].lower()
        return newword == newword[::-1]

        