class Car:
    weight=1000
    def __init__(self,weight,driver):
        self.weight=weight
        self.driver=driver
class Person:
    weight=100
    def __init__(self,weight):
        self.weight=weight
print(type(Person))
p=Person(150)
print(type(p))
c=Car(2000,p)
print(Car.weight)
print(c.weight)
print(c.driver.weight)
