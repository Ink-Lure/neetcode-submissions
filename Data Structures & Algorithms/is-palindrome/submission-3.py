class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = re.sub(r'[^a-zA-Z0-9]', '',s.lower().replace(" ", ""))

        return fs == fs[::-1]
        