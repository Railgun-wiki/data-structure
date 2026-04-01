#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        data = [-1] * k
        self.data = data
        self.start = 0
        self.end = 0
        self.size = k
        self.container = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.start = (self.start - 1) % self.size
        self.data[self.start] = value
        self.container += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end = (self.end + 1) % self.size
        self.data[self.end - 1] = value
        self.container += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.size
        self.container -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end = (self.end - 1) % self.size
        self.container -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.start]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.end - 1]
        

    def isEmpty(self) -> bool:
        if self.start == self.end and self.container == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.start == self.end and self.container != 0:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

