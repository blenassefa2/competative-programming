class Solution:
    def isValid(self, s: str) -> bool:
        lefts = ["[","{","("]
        rights = ["]","}",")"]
        stack =[]
        string = s
        balanced = True
        for i in string:
            
            if i in lefts:
                stack.append(i)
            elif i in rights:
                index = rights.index(i)
                if not bool(stack):
                    balanced = False
                    break
                if stack[-1] == lefts[index]:
                    stack = stack[:len(stack) -1]
                else:
                    balanced = False
                    break
        if bool(stack):
            balanced = False
        return balanced