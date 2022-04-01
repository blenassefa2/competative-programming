class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        op_br = []
        unlocked = []
        for i in range(len(s)):
            if s[i] == ')' and locked[i] =='1':
                if op_br:
                    op_br.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
            elif s[i] == '(' and locked[i] == '1':
                op_br.append(i)
            else:
                unlocked.append(i)
        for j in range(len(op_br)):
            if not unlocked:
                break
            if op_br[-1] > unlocked[-1]:
                return False
            
            op_br.pop()
            unlocked.pop()
        return (len(unlocked)%2 == 0) and len(op_br) == 0