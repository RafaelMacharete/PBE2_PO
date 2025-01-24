class Rectangle():
    def __init__(self, rectangle_h, rectangle_w):
        self.heigth = rectangle_h
        self.width = rectangle_w
    
    def rectangle_area(self):
        return self.heigth * self.width
    
    def rectangle_perimeter(self):
        return 2 *(self.heigth + self.width)
    
rectangle1 = Rectangle(5,2)

print(rectangle1.rectangle_area())
print(rectangle1.rectangle_perimeter())