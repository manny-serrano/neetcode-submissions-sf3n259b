class Solution:
    def isValid(self, s: str) -> bool:

        valid = {")":"(", "}":"{", "]":"["}

        stack = []
        for i in range(len(s)):
            if s[i] in valid.values():
                stack.append(s[i])
            elif s[i] in valid:
                if not stack or stack[-1] != valid[s[i]]:
                    return False

                else:
                    stack.pop()
        return len(stack) == 0

        
        