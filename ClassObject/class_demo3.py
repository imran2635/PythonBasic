class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.skills = []

    def person_info(self):
        return f'Name: {self.name} \nAge: {self.age} \nCity: {self.city}'

    def add_skills(self, skill):
        self.skills.append(skill)


my_obj = Person("Batman", 20, "Dhaka")
print(my_obj.person_info())

my_obj.add_skills("Python")
my_obj.add_skills("C++")
my_obj.add_skills("Java")
my_obj.add_skills("Testing")
print(my_obj.skills)

