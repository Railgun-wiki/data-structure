class Rectangle:
    def __init__(self, width, height):
        # TODO: 初始化属性
        self.width = width
        self.height = height
        pass

    def area(self):
        # TODO: 计算面积
        return self.width * self.height
        pass

    def perimeter(self):
        # TODO: 计算周长
        return 2 * (self.width + self.height)
        pass

    def is_square(self):
        # TODO: 判断是否为正方形
        if self.width == self.height:
            return True
        else:
            return False
        pass

# 测试
rect = Rectangle(5, 10)
print(rect.area())        # 50
print(rect.perimeter())   # 30
print(rect.is_square())   # False