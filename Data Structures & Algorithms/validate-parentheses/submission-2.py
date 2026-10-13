class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        stack = []
        mapping = { ")": "(", "}": "{", "]": "["}
        for ch in s :
            if ch in mapping: #check for closing brackets
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)   
        return not stack                        
        