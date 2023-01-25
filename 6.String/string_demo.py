letter = "a"
name = "smith"
tax = '12.22'
age = 20

message = '''
Hello world..
How are you today
what are you doing.
'''

# 6.String concatenation
print(name + " " + tax + " " + str(age))

# Escape Sequence
"""
\n: new line
\t: tab
\r: carriage return
\b: backspace
\': single quote
\": double quote
"""
# print("Hello dhaka. \n Bangladesh")
print("Days\tTopics\tExercise")
print("1\tPython\t10")
print("2\tPython\t10")
print("3\tPython\t10")
print("4\tPython\t10")
print("5\tPython\t10")

print('shakespeare Quote \r "We know what we are, but know not what we may be.(\\)"')

# 6.String Formatting
print(f"{name} {tax} {age}")

first_name = "kevin"
last_name = "abc12"
my_age = 30

formatted_string = 'My full name: {} {} \nMy age: {}'.format(first_name, last_name, my_age)
print(formatted_string)

# 6.String builtin function
print(message.replace("world", "Universe"))
print(first_name.capitalize())
print(first_name.upper())
print(first_name.lower())
print(len(first_name))

print(tax.isalnum())
print(first_name.isdigit())
print(first_name.isnumeric())
print(first_name.islower())
print(first_name.isupper())