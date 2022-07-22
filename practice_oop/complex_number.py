class ComplexNumber:
    def __init__(self, r=0, i=0):
        print("I'll execute automatically if a new object is being created.")
        self.r = r
        self.i = i

    def get_data(self):
        print(f"{self.r} + {self.i}j")


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data method
num1.get_data()

# Create another ComplexNumber object
num2 = ComplexNumber(5)
# Create a new attribute
num2.attr = 10
# Call get_data method
num2.get_data()

print(num2.r, num2.i, num2.attr)

# num1 object doesn't have any attribute.
# If call AttributeError will generate
# print(num1.attr)

# Deleting num3.i attribute &  num3.get_data method
num3 = ComplexNumber(5, 7)
# del num3.i
# print(num3.i)
# del ComplexNumber.get_data
num3.get_data()

# Object itself can be deleted
num4 = ComplexNumber(1, 2)
del num4
# num4
