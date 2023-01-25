class Calculator:
    def summation(self, number1, number2):
        return number1 + number2

    def subtract(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        return number1 / number2


if __name__ == '__main__':
    calculator_obj = Calculator()
    print(calculator_obj.summation(10, 20))
    print(calculator_obj.subtract(10, 20))
    print(calculator_obj.multiply(10, 20))
    print(calculator_obj.divide(10, 5))
