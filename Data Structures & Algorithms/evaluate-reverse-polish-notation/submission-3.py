class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polishset = ('+', '-', '*', '/')
        numbers = []

        for i,value in enumerate(tokens):
            if value not in polishset:
                numbers.append(int(value))
            else:
                r,l = numbers.pop(), numbers.pop()
                if value == '+':
                    numbers.append(l+r)
                elif value == "-":
                    numbers.append(l-r)
                elif value == '*':
                    numbers.append(l*r)
                elif value == '/':
                    numbers.append(int(l/r))

        return numbers.pop()

            

        