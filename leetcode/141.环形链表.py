#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 双指针，如果有环则快慢指针必定相遇
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not(fast and fast.next):
                return False
            slow = slow.next
            # fast步数为slow*2
            fast = fast.next.next
        return True
# @lc code=end

