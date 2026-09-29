class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        for c in s:
            if c in mapS:
                mapS[c] = mapS[c] + 1
            else:
                mapS[c] = 1
        
        for c in t:
            if c in mapT:
                mapT[c] = mapT[c] + 1
            else:
                mapT[c] = 1

        return mapS == mapT