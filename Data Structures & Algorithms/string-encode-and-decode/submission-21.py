class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j]) # this is the length which is the prefix integer but need to convert it to type int
            #remeber j is # delimeter
            result.append(s[j+1:j+1+length]) #from j+1 to j+1+length of string
            #need to update i to keep iterating, needit to be start of next word
            i=j+1+length
        return result