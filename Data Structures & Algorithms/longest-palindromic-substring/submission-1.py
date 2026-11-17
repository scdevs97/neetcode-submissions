class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        
        isPalindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            isPalindrome[i][i] = True
            if i > 0:
                isPalindrome[i][i-1] = True
        
        maxWindowSize = 1
        longestPalindrome = s[0]
        for windowSize in range(2, len(s) + 1):
            for i in range(len(s)):
                if i + windowSize > len(s):
                    continue
                isPalindrome[i][i + windowSize - 1] = isPalindrome[i+1][i + windowSize - 2] and s[i] == s[i + windowSize - 1]
                if isPalindrome[i][i + windowSize - 1] and windowSize > maxWindowSize:
                    maxWindowSize = windowSize
                    longestPalindrome = s[i:i + windowSize]
        
        return longestPalindrome

            

        