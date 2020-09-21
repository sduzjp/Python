class Car:
    color='gray'
    def describeCar(self):
        return 'A cool '+Car.color+' car '
    def describeSelf(self):
        return 'A cool '+self.color+' car '
nona=Car()
print(nona.describeCar())
print(nona.describeSelf())
print(nona.color)
lola=Car()
lola.color='plaid'
print(lola.describeCar())
print(lola.describeSelf())
print(lola.color)
print(nona.describeSelf())
nona.size='small'
print(lola.size)
Car.size='big'
print(lola.size)
print(nona.size)
