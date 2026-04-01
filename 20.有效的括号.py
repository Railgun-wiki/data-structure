#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        q = LifoQueue()
        
        for c in s:
            if c == '(':
                q.put(c)
            elif c == ')':
                if q.empty() or q.get() != '(':
                    return False
            elif c == '{':
                q.put(c)
            elif c == '}':
                if q.empty() or q.get() != '{':
                    return False
            elif c == '[':
                q.put(c)
            elif c == ']':
                if q.empty() or q.get() != '[':
                    return False
        if q.empty():
            return True
        else:
            return False
        
# @lc code=end

