# Dương Phúc Hợp msv: 245752021610047
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius   # gán giá trị bán kính truyền vào cho đối tượng
    # Tính diện tích hình tròn: S = π * r^2
    def area(self):
        return math.pi * (self.radius ** 2)    
    # Tính chu vi hình tròn: C = 2 * π * r
    def circumference(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
