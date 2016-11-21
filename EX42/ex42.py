class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object)
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rove = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

may.pet = satan

fran = Employee("Frank", 120000)

frank.pet = Rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
