class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        s_lengths = []
        for s in strs:
            s_lengths.append(len(s))
        s_lengths_str = ','.join([str(s_length) for s_length in s_lengths])
        return s_lengths_str + '#' + ''.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = []
        s_lengths_str, strs_combined = s.split('#', maxsplit=1)
        print(s)
        s_lengths = [int(l) for l in s_lengths_str.split(',')]
        i = 0
        for l in s_lengths:
            strs.append(strs_combined[i: i+l])
            i = i + l
        return strs

       
