## Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal(object):
    pass 

## Dod is-a Animal 
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name 
        self.name = name 

## Cat is-a Animal 
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name 
        self.name = name 

## Person is-a object 
class Person(object):

    def __init__(self, name):
        ##Person has-a name 
        self.name = name 

        ##Person has-a pet of some kind
        self.pet = None 

## Employee is-a person 
class Employee(Person):

    def __init__(self, name, salary):
        ## super use parent class's function hmm what is this stange magic
        super(Employee, self).__init__(name)
        ## Employee has-a salary 
        self.salary = salary 

## Fish is-a object 
class Fish(object):
    pass 

## Salmon is-a fish 
class Salmon(Fish):
    pass 

## Halibut is-a fish 
class Halibut(Fish):
    pass 


## rover is-a Dog 
rover = Dog("Rover")

## satan is-a Cat 
satan = Cat("Satan")

## mary is-a Person 
mary = Person("Mary")

## mary has-a pet name is satan 
mary.pet = satan 

## frank is-a Employee and salary is 120000
frank = Employee("Frank", 120000)

## frank has-a pet, name is rover 
frank.pet = rover 

## slipper is-a fish 
slipper = Fish()

## crouse is-a Salmon 
crouse = Salmon()

## harry is-a Halibut 
harry = Halibut()
