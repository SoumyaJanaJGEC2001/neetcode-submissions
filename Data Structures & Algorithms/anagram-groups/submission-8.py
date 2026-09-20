class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for i in strs:
            w = "".join(sorted(i))
            if w in out:
                out[w].append(i)
            else:
                out[w] = [i]
        return list(out.values())
