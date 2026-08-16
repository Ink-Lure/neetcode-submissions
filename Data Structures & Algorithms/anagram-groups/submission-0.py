class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            if "".join(sorted(string)) in seen:
                seen["".join(sorted(string))].append(string)
            else:
                seen["".join(sorted(string))] = [string]
        return [seen[x] for x in seen]
        