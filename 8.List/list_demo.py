# List is a collection of different data types which is ordered and changeable(mutable)
# List are written with square brackets[].
# List can be empty or not

fruits = ['apple', 'orange', 'banana']
cities = ['Dhaka', 'paris', 'NY', 'London']
countries = ['USA', 'Canada', 'France', 'Germany', 'UK', 'Bangladesh', "Uganda", 'Nepal', 'Bhutan']

# Accessing the list
United_states = countries[0]
print(United_states)

# Slicing the list
powerful_countries = countries[0:5]
print(powerful_countries)

powerless_countries = countries[5:]
print(powerless_countries)

# Modifying/replacing the list
powerful_countries[4] = 'China'
print(powerful_countries)

# Checking item in the list
print('Bangladesh' in countries)

# Adding item in the list
powerful_countries.append('India')
print(powerful_countries)

# Removing item in the list
powerful_countries.remove('Canada')
print(powerful_countries)

# Insert item in the list
powerful_countries.insert(1, 'Canada')
print(powerful_countries)

# Removing item in the list
countries.pop()
print(countries)

# Length of list
powerful_countries_count = len(powerful_countries)
print(powerful_countries_count)

# Sorting the list
countries.sort()
print(countries)

# reverse the list
countries.reverse()
print(countries)

# Clear the list
countries.clear()
print(countries)
