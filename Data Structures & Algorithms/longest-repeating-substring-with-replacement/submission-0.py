class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s):
            return len(s)
        
        windowStart = 0
        windowEnd = 0 
        charFrequencyInWindow = defaultdict(int)
        longestLength = 0

        while windowEnd < len(s):
            newChar = s[windowEnd]
            charFrequencyInWindow[newChar] += 1
            while max(charFrequencyInWindow.values()) + k < windowEnd - windowStart + 1:
                charToRemove = s[windowStart]
                windowStart += 1
                charFrequencyInWindow[charToRemove] -= 1
            longestLength = max(longestLength, windowEnd - windowStart + 1)
            windowEnd += 1
            
        return longestLength

    