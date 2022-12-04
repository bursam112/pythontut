class Organism:
    alive = True


class Animal(Organism):

    def eat(self):
        print(f'The animal is eating')

    def sleep(self):
        print(f'The animal is sleeping')


class Prey(Animal):

    def flee(self):
        print('The prey is fleeing!')


class Predator(Animal):

    def hunt(self):
        print('The predator is hunting...')


class Rabbit(Prey):

    def run(self):
        print('This rabbit is running')


class Fish(Prey, Predator):

    def swim(self):
        print('This fish is swimming')


class Hawk(Predator):

    def fly(self):
        print('This hawk is flying')


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
print()

print(rabbit.alive)
fish.eat()
hawk.sleep()
print()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
print()

rabbit.run()
fish.swim()
hawk.fly()
