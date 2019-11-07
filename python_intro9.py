#Inheritance/Polymorphism

class Animal:                       #Base class
    def __init__(self):
        self.__numberoflegs = 4

    def make_noise(self):
        pass

class Dog(Animal):                  #Dog is a sub class of Animal
    def make_noise(self):           #make_noise method override
        print("Woof, woof!")

class Cat(Animal):                  #Cat is a sub class of Animal
    def make_noise(self):           #make_noise method override
        print("Meow, meow!")

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)

    def make_noise(self):
        print("Chirp, chirp!")

class Talk:
    def to(self, animal):
        animal.make_noise()

if __name__ == '__main__':
    animals = [Dog(), Cat(), Bird()]
    talk = Talk()
    for count in list(range(3)):
        talk.to(animals[count])    #Polymorphism in action
                                   #any object that implements the make_noise method can be operated on by Talk