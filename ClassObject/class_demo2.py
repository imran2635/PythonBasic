class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def person_info(self):
        return f'Name: {self.name} \nAge: {self.age} \nCity: {self.city}'


my_obj = Person("Batman", 20, "Dhaka")
print(my_obj.person_info())

my_obj2 = Person("Superman", 30, "NY")
print(my_obj2.person_info())

my_obj3 = Person("Spiderman", 40, "CA")
print(my_obj3.person_info())