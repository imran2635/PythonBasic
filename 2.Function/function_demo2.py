def tk_to_rupee(rupee_conversion_rate):
    user_input = float(input("Enter TK you and to Convert Rupee: "))
    result = float(user_input * rupee_conversion_rate)
    print("Your Rupee: " + str(result))


def tk_to_dollar():
    dollar_conversion_rate = .0096
    user_input = float(input("Enter TK you and to Convert Dollar: "))
    result = float(user_input * dollar_conversion_rate)
    print("Your Dollar: " + str(result))


#tk_to_rupee(.88)
#tk_to_dollar()

def summation(number1,number2):
    sum = number1 + number2
    print(sum)


summation(20,50)
summation(100,200)
summation(1000,500)
summation(-100,-50)