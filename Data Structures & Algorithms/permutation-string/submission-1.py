class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True
        if len(s1) > len(s2):
            return False
        
        s1CharFreq = [0] * 26
        for c in s1:
            s1CharFreq[ord(c) - ord('a')] += 1
        
        windowCharFreq = [0] * 26
        for i in range(len(s1)):
            currChar = s2[i]
            windowCharFreq[ord(currChar) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            if s1CharFreq == windowCharFreq:
                return True
            if i + len(s1) < len(s2):
                newCharToAdd = s2[i + len(s1)]
                charToRemove = s2[i]
                windowCharFreq[ord(newCharToAdd) - ord('a')] += 1
                windowCharFreq[ord(charToRemove) - ord('a')] -= 1
        return False


