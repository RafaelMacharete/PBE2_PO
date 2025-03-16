class Triangle():
    def __init__(self, a_side, b_side, c_side):
        self.a = a_side
        self.b = b_side
        self.c = c_side

    def verify_existence(self):
        if (self.a + self.b > self.c and 
            self.b + self.c > self.a and 
            self.a + self.c > self.b):
            return True
        return False


triangle1 = Triangle(10, 0, 0)

print(f'Does the triangle exist?\n{triangle1.verify_existence()}')