#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0:
            ans.append("")
        else:
            for i in range(n):
                for left in self.generateParenthesis(i):
                    for right in self.generateParenthesis(n - 1 - i):
                        ans.append("(" + left + ")" + right)
        return ans
# @lc code=end

