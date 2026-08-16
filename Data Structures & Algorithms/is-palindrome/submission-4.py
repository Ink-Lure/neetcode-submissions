class Solution:
    def isPalindrome(self, s: str) -> bool:
        return re.sub(r'[^a-zA-Z0-9]', '',s.lower().replace(" ", "")) == re.sub(r'[^a-zA-Z0-9]', '',s.lower().replace(" ", ""))[::-1]
        