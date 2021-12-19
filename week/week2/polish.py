class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators =["+", "-","*","/"]
        stack = []
        for i in tokens:
        
            if i not in operators:
                stack.append(int(i))
            else:
                index = operators.index(i)
                x = stack[-2]
                y = stack[-1]
                stack = stack[:-2]
                if index == 0:
                    stack.append(x+y)
                elif index == 1:
                    stack.append(x-y)
                elif index == 2:
                    stack.append(x*y)
                else:
                    stack.append(int(x/y))
        ans = stack[0]
        return ans