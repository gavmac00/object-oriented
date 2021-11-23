# Object oriented programming

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say") #note Cat didn't use this function when it was called despite having the same function name

class Cat(Pet): #inherenting the upper level class Pet

    def __init__(self,name,age,colour):
        super().__init__(name,age) #try commenting out this line, calls parent name and age initialisation, it is important and we must call it
        self.colour = colour

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, and I am {self.colour}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()

c = Cat("Bill", 34, "Blue")
c.show()

d = Dog("Jill", 25)
d.speak()
