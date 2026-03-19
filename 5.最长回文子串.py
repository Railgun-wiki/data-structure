#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ansright, ansleft = 0, 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 2 > ansright - ansleft:
                ansright, ansleft = right - 1, left + 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 2 > ansright - ansleft:
                ansright, ansleft = right - 1, left + 1
        return s[ansleft:ansright + 1]

# @lc code=end


