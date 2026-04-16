class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        polishset = ('+', '*', '/', '-')
        for i, value in enumerate(tokens):
            if value not in polishset:
                stack.append(int(value))
            else:
                r,l = stack.pop(), stack.pop()
                if value == "-":
                    stack.append(l-r) 
                elif value == "+":
                    stack.append(l+r)
                elif value == "*":
                    stack.append(l*r)
                elif value == "/":
                    stack.append(int(l/r))   
        return stack[-1]        
            
                

