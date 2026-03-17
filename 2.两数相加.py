#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        ans_head = ans
        addon = 0
        
        while l1 or l2:
            ans.val += addon
            if l1:
                ans.val += l1.val
                l1 = l1.next
            if l2:
                ans.val += l2.val
                l2 = l2.next
            addon = ans.val // 10
            ans.val %= 10
            if l1 or l2:
                ans.next = ListNode(0)
                ans = ans.next
        if addon:
            ans.next = ListNode(addon)
        return ans_head
# @lc code=end

