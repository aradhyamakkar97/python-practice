class Dog:

    num_of_dogs = 0

    def __init__(self,name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def  getNumOfDogs():
        print('there are currently {} dogs'.format(Dog.num_of_dogs))

def main():
    spot = Dog("Spotty")
    kutta = Dog("harami")
    spot.getNumOfDogs()

main()
