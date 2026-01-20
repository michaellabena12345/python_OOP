class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculation(self):
         return self.width  * self.height 
    def __str__(self):
        return f"rectangle {self.width} x {self.height}"

calculate = Rectangle(5, 6)
print(calculate)
print("area", calculate.calculation())