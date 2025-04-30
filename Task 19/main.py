class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


factor = int(input("Enter the multiplication factor: "))
number = int(input("Enter the number to multiply: "))

m = Multiplier(factor)


print("Is object callable?", callable(m))


result = m(number)
print(f"Result: {factor} x {number} = {result}")
