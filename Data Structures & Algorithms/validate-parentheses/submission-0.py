class Solution:
    def isValid(self, s: str) -> bool:
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
        return True if not stack else False                        
        