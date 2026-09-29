class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            final_count = tuple(count)
            if final_count in map:
                map[final_count].append(s)
            else:
                map[final_count] = [s]
        
        return_list = []
        for i in map:
            return_list.append(map[i])

        return return_list