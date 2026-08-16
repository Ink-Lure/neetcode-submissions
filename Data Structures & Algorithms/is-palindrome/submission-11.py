class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = re.sub(r'[^a-zA-Z0-9]', '',s.lower().replace(" ", ""))

        for i in range(math.ceil(len(fs) / 2)):
            if fs[i] != fs[len(fs) - i - 1]:
                return False

        return True
        