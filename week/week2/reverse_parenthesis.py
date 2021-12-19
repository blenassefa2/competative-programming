class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ""

        for i in s:
            
            if i != ")":
                stack+=i
            else:
                reverse =""
                while stack[-1] != "(":
                    reverse +=stack[-1]
                    stack = stack[:-1]
                stack = stack[:-1]
                stack +=reverse
        return stack