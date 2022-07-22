class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter_calculate(self):
        p = self.a + self.b + self.c
        return p


t1 = Triangle(3, 4, 5)
print("Perimeter of triangle is: " + str(t1.perimeter_calculate()))
