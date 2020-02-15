class Calculator:

    def __init__(self):
        pass

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        if num1 > num2:
            return num1 - num2
        elif num1 < num2:
            return num1 - num2
        else:
            return 0

    def multiplication(self, num1, num2):
        return num1 * num2


    def division(self, num1, num2):
        if num1 > num2:
            return num1 / num2
        elif num1 <= num2:
            try:
                return num1 / num2
            except ZeroDivisionError:
                print "Cannot divide by zero"
                raise
