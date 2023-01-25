# Tuple is a collection of different data types which is ordered and unchangeable(immutable)
# Tuples are written with round brackets().

person = ('Mr', 'smith', 'Dhaka', 30, 20.2)
print(person)

# Accessing Item
first_name = person[0]
last_name = person[1]
address = person[2]
age = person[3]
print(first_name)

print(f"My Old Address: {address}")

# Checking an item in Tuple
print('Dhaka' in person)
print('Bangladesh' in person)

# joining
fruits = ('apple', 'orange', 'banana')

new_tuple = person + fruits
print(new_tuple)



