# from car import Car

# car_1 = Car('Chevy', 'Corvette', 2021, 'blue')
# car_2 = Car('Ford', 'Mustang', 2022, 'red')

# Car.wheels = 2
# print(car_1.wheels)
# print(car_2.wheels)


class Animal:
    alive = True

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal is sleeping')


class Rabbit(Animal):
    def run(self):
        print('This rabbit is running')


class Fish(Animal):
    def swim(self):
        print('This fish is swimming')


class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()