# Object oriented programming

class Dog:
    def __init__(self, name, age): #instantiate object
        self.name = name #self invisibly passes the reference
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("harvey", 13)
print(d.get_name())