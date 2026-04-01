#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 将两个列表视为两个队列，用双指针取出较小的头部元素放入nums1
        nums1c = nums1.copy()
        n1 = n2 = 0
        for i in range(m + n):
            if n1 < m and n2 < n:
                if nums1c[n1] < nums2[n2]:
                    nums1[i] = nums1c[n1]
                    n1 += 1
                else:
                    nums1[i] = nums2[n2]
                    n2 += 1
            elif n1 < m:
                nums1[i] = nums1c[n1]
                n1 += 1
            else:
                nums1[i] = nums2[n2]
                n2 += 1
# @lc code=end

