"""
1. Builtin functions
2. Custom
"""


def summation():
    number1 = 10
    number2 = 20
    sum = number1 + number2
    print(sum)


#summation()


def subtract():
    number1 = 10
    number2 = 20
    difference = number1 - number2
    print(difference)


#subtract()

def multiply():
    number1 = 10
    number2 = 20
    product = number1 * number2
    print(product)

#multiply()

def divide():
    number1 = 10
    number2 = 20
    quotient = number1 / number2
    print(quotient)

#divide()


def dhaka():
    print("dhaka123")


#dhaka()


def tk_to_rupee():
    rupee_conversion_rate = .85
    user_input = float(input("Enter TK you and to Convert Rupee: "))
    result = float(user_input * rupee_conversion_rate)
    print("Your Rupee: " + str(result))
    print(result)


#tk_to_rupee()


def tk_to_dollar():
    dollar_conversion_rate = .0096
    user_input = float(input("Enter TK you and to Convert Dollar: "))
    result = float(user_input * dollar_conversion_rate)
    print("Your Dollar: " + str(result))


#tk_to_dollar()

dhaka()
summation()
subtract()
multiply()
divide()
tk_to_rupee()
tk_to_dollar()
