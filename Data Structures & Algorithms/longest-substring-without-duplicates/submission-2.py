class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        charIndex = {}
        windowStart = 0
        windowEnd = 0
        longestLength = 1

        while windowEnd < len(s):
            if s[windowEnd] in charIndex and charIndex[s[windowEnd]] >= windowStart:
                longestLength = max(longestLength, windowEnd - windowStart)
                windowStart = charIndex[s[windowEnd]] + 1
            charIndex[s[windowEnd]] = windowEnd    
            windowEnd += 1
        
        longestLength = max(longestLength, windowEnd - windowStart)
        return longestLength
