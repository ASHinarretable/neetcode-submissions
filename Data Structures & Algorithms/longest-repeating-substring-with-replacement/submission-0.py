class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #so make a dynamic sliding window, calculate the frequenncy of letters 
        #highest freq letter is the winner so teh window must replace 
        #the no of letters btwn left and right pointer and return the lenght of sliding window
        window,left,maxm = 0, 0, 0
        freq = {}
        for right in range(len(s)):
            #calculate frequency
            freq[s[right]] = 1 + freq.get(s[right], 0)
            #calculate max freq
            maxm = max(maxm, freq[s[right]])
            if (right - left + 1) -maxm > k:
                freq[s[left]] -= 1
                left += 1
            window = max(window, right - left +1)
        return window     