class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer approach
        left = 0
        n = len(s) - 1
        right = n 
        
        while left < right:
            if not self.alphaNum(s[left]):
                left += 1
                continue

            if not self.alphaNum(s[right]):
                right -= 1
                continue  

            if s[left].lower() != s[right].lower() :
                    return False
      
            left,right = left +1, right -1

        return True                 

    def alphaNum(self, c):
        return ( 
            (ord('A') <= ord(c) <= ord('Z') ) or
            (ord('a') <= ord(c) <= ord('z') ) or
            (ord('0') <= ord(c) <= ord('9') ) 
            )