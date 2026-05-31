class Solution:
    def isnum(self, num):
        try:
            float(num)
            return True
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if self.isnum(c):
                stack.append(int(c))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num2 - num1)
                elif c == '*':
                    stack.append(num1 * num2)
                elif c == '/':
                    stack.append(int(num2/num1))
        return stack[0]            
        