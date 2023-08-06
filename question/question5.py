class Solution:
    def getPalindrom(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i = i - 1
            j = j + 1
        return i + 1, j - 1

    def longestPalindrome(self, s: str) -> str:
        final_left = 0
        final_right = 0
        for i in range(len(s)):
            left1, right1 = self.getPalindrom(s, i, i)
            left2, right2 = self.getPalindrom(s, i, i + 1)
            if right1 - left1 > final_right - final_left:
                final_left, final_right = left1, right1
            if right2 - left2 > final_right - final_left:
                final_left, final_right = left2, right2
        return s[final_left : final_right + 1]