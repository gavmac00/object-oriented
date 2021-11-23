class Person:
    number_of_people = 0
    gravity = -9.81 # no dependancies if inside class, no globals

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1 # increases number_of_people by 1 each time a new instance is created

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())