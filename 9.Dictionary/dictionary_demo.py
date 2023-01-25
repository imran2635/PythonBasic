# Dictionary is a collection of unordered, modifiable, paired(key:value) data type.
# Dictionary are written with second brackets {}

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

# Accessing
print(person["name"])
print(person["age"])
print(person["city"])
print(person["skills"][0])
print(person["hobby"][1])
print(person["full_address"]["old_house"] ["old_house_street"])
