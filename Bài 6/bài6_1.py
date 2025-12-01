# Dương Phúc Hợp msv: 245752021610047
import math
class Circle:
    def __init__(self, radius): # seft là tham số đầu tiên của mói phương thức trong lớp. Nó đại diện cho chính đối tượng được tạo
        self.radius = radius  # Dòng này gán giá trị bán kính được truyền vào cho thuộc tính radius của đối tương
    def area(self):
        return math.pi * (self.radius ** 2)
c = Circle(5)
print("Diện tích hình tròn:", c.area())
