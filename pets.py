class Pet:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Pet):

    def __init__(self,name,age):
        super().__init__(name,age) # super class methods can be run like this

    def talk(self):
        return "Meowww"

class Dog(Pet):
    def __init__(self,name,age):
        super().__init__(name,age)

    def talk(self):
        return "I AM KUTTAA"

def Main():
    pets = [Cat("jess",3),Dog("Jack",2),Cat("Fred",7),Pet("thePet",1)]

    for pet in pets:
        print ("Name: "+pet.name+", Age: "+str(pet.age)+ ", say : "+pet.talk())


if __name__ == '__main__':
    Main()
