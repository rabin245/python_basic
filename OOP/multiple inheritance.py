# child class is derived from more than one classes

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print('This animal is hunting')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.hunt()