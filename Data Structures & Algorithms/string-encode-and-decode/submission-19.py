class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"/{len(x)}.{x}" for x in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        list = [s[i:l+i] for (i,l) in [(i + re.search("^/[0-9]+.", s[i:]).span()[1], int(re.search("^/[0-9]+.", s[i:]).group()[1:-1])) for i, x in enumerate(s) if x == "/" and bool(re.search("^/[0-9]+.", s[i:]))]]

        print(list)
        return list