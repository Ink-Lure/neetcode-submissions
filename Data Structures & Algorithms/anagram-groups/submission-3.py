class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            seen.setdefault(''.join(sorted(string)), []).append(string)
        return list(seen.values())
        