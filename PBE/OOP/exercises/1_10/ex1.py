class Circle():
    def __init__(self, id, circle_radius):
        self.id = id
        self.radius = circle_radius

    def circle_area(self):
        self.area = 3.14 * self.radius ** 2
        print('A=',self.area)
    
    def circle_circumference(self):
        self.circumference = 2 * 3.14 * self.radius
        print('C=',self.circumference)

circle1 = Circle(0, 5)

circle1.circle_area()
circle1.circle_circumference()