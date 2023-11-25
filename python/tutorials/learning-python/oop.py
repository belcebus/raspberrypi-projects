class Person:
    species = 'H. sapiens'

Person.alive = True

print(Person.species)
print(Person.alive)

man = Person()

print(man.species)
print(man.alive)

Person.alive = False

print(man.species)
print(man.alive)

man.name='John'

print(man.name)
#print(Person.name)

#del man.alive

print(man.alive)

class Square():
    side = 2
    def square_area(self):
        return self.side**2

square = Square()

print(square.side)
print(square.square_area())
print(Square.side)
print(Square.square_area(square))

Square.side=3

print(square.side)
print(square.square_area())
print(Square.side)
print(Square.square_area(square))


class Price():
    """Class for calculating the final price of a product."""
    def final_price(self, vat, discount=0):
        """Return the final price of the product."""
        return self.net_price * (1 + vat) * (1 - discount)

price = Price()

print(price.__doc__)
print(price.final_price.__doc__)

price.net_price = 100
print(price.final_price(0.23, 0.1))

class Rectangle():

    sideA=0
    sideB=0
    
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
    
    def area(self):
        return self.sideA * self.sideB

r1 = Rectangle(2, 3)
print(r1.area())

# continuamos con el ejemplo de la clase Engine

class Engine():
    cilindros=0
    def start(self):
        pass
    def stop(self):
        pass

class V8Engine(Engine): #is a Engine
    cilindros=8
    pass

class ElectricEngine(Engine): #is a Engine
    pass

class Car():

    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()
        
    def start(self):
        print(
            'Starting engine {0} with {2} cilinders for car {1}'.format(
                self.engine.__class__.__name__,
                self.__class__.__name__,
                self.engine.cilindros,
            )
        )
        self.engine.start()
    
    def stop(self):
        self.engine.stop()

class RaceCar(Car): #is a Car
    engine_cls=V8Engine

class FamilyCar(Car): #is a Car
    engine_cls = ElectricEngine

class F1Car(RaceCar):
    engine_cls=V8Engine

car = Car()
racecar = RaceCar()
familycar=FamilyCar()
f1car = F1Car()

cars = [car,racecar,familycar,f1car]

for car in cars:
    car.start()

    



class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

class EBook(Book):

    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

eBook = EBook('Learning Python', 'Mark Lutz', 500, 'pdf')

print(eBook.title)
print(eBook.author)
print(eBook.pages)
print(eBook.format)
print(eBook.__dict__)

########################

class Shape:

    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError
    def geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))
    
class Polygon(Shape, Plotter):

    geometric_type = 'Polygon'

