
class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1
p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("jill")

Person.number_of_people = 8

print(p2.number_of_people) # what is the type of p2?: Person,  Does p2 have an attribute 'number_of_people'?: No,  Does the class have an attribute called 'number_of_people'? : Yes!
print(p1.number_of_people)