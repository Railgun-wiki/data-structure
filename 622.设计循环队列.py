#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        data = [-1] * k
        self.data = data
        self.start = 0
        self.end = 0
        self.size = k
        self.container = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end = (self.end + 1) % self.size
        self.data[self.end - 1] = value
        self.container += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.size
        self.container -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.start]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.end - 1]
        

    def isEmpty(self) -> bool:
        if self.container == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.container != 0 and self.start == self.end:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

