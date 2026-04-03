from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a list as the default value for new keys
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique key for all its anagrams
            key = "".join(sorted(s))
            anagram_map[key].append(s)
            
        # Return only the grouped values
        return list(anagram_map.values())
