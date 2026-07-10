# 3)	Create a Calculator class with a static method to calculate the square of a number.
class Calculator:
    @staticmethod
    def sq(num):
        return (num**2)
print(Calculator.sq(5))