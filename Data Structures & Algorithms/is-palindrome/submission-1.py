class Solution:
    def isPalindrome(self, s: str) -> bool:
        return list(re.sub(r'[^a-zA-Z0-9]', '',s.lower().replace(" ", ""))) == list(re.sub(r'[^a-zA-Z0-9]', '',s.lower().replace(" ", "")))[::-1]
        