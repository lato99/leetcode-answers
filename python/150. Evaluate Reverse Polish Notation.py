class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:

            if token == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(str(num1+num2))
            elif token == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(str(num2-num1))
            elif token == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(str(num2*num1))
            elif token == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(str(int(num2/num1)))
            else:
                stack.append(token)
        return int(stack.pop())