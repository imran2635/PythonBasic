# for i in range(0,11,4):
#    print(i)

"""
start_number = int(input("Enter Start Number: "))
end_number = int(input("Enter End Number: "))

if start_number <= end_number:
    for i in range(start_number, end_number, 2):
        print(start_number)
        start_number += 2
else:
    print("Start Number must be less or equal to End Number")
"""

"""
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in number:
    print("Iteration " +str(i))
"""

"""
language = "python"
for i in language:
    print(i)
"""

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Java", "C#"],
    "full_address":
        {
            "street": "123 Main Street",
            "house": "123/ad",
            "old_house":
                {
                    "old_house_street": "123 old avenue"
                }
        },
    "hobby": ("Gardening", "Travel", "Photography")
}

for key in person:
    print(key)


# All key and value
def get_all_keys_values(dictionary_name):
    for key, value in dictionary_name.items():
        print(str(key) + " : " + str(value))


# Specific key
def get_specific_key_from_dictionary(dictionary_name, specific_key):
    for key, value in dictionary_name.items():
        if key == specific_key:
            print(str(key) + " : " + str(value))


# Create a List with all keys
def create_list_from_dictionary_keys(dictionary_name):
    key_list = []
    for key in dictionary_name.keys():
        key_list.append(key)
    print(key_list)


# Create a List with all values
def create_list_from_dictionary_value(dictionary_name):
    value_list = []
    for value in dictionary_name.values():
        value_list.append(value)
    print(value_list)


create_list_from_dictionary_value(person)
create_list_from_dictionary_keys(person)
get_specific_key_from_dictionary(person, "city")
get_specific_key_from_dictionary(person, "name")
get_all_keys_values(person)
