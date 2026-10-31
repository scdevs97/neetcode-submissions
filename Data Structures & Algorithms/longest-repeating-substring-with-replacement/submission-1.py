class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s):
            return len(s)
        
        windowStart = 0
        windowEnd = 0 
        charFrequencyInWindow = defaultdict(int)
        maxFrequencyInWindow = 0
        longestLength = 0

        while windowEnd < len(s):
            newChar = s[windowEnd]
            charFrequencyInWindow[newChar] += 1
            maxFrequencyInWindow = max(maxFrequencyInWindow, charFrequencyInWindow[newChar])
            while maxFrequencyInWindow + k < windowEnd - windowStart + 1:
                charToRemove = s[windowStart]
                windowStart += 1
                charFrequencyInWindow[charToRemove] -= 1
                maxFrequencyInWindow = max(charFrequencyInWindow.values())
            longestLength = max(longestLength, windowEnd - windowStart + 1)
            windowEnd += 1
            
        return longestLength

    