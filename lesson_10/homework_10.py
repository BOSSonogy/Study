# Task 1

from abc import ABC, abstractmethod
from math import pi
from math import sqrt

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def recommend(self):
        print(f"Namaste. I'm {self.name} with nice {self.salary}$ salary from {self.department}.")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def recommend(self):
        print(f"Hello there. I'm {self.name} with nice {self.salary}$ salary with {self.programming_language} skills.")

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def recommend(self):
        print(f"Hi. I'm {self.name} with {self.salary}$ salary from {self.department}."
              f" And it's {self.programming_language} team. Our size is {self.team_size} employees.")

new_manager = Manager('Bob', 1200, 'UI team')
new_teammate = Developer('John', 1500, 'Rust')
our_lead = TeamLead('Malcolm', 2600, 'Main team', 'Rust and C#', 13)


new_manager.recommend()
new_teammate.recommend()
our_lead.recommend()


# Task 2

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Rhombus(Figura):
    def __init__(self, side_a, height_h):
        self._side_a = side_a
        self._height_h = height_h

    def area(self):
        rhombus_area = self._side_a * self._height_h
        print(f'Rhombus area = {rhombus_area}')

    def perimetr(self):
        rhombus_per = self._side_a * 4
        print(f'Rhombus perimetr = {rhombus_per}')


class Quadrangle(Figura):
    def __init__(self, side_a, side_b):
        self._side_a = side_a
        self._side_b = side_b

    def area(self):
        quard_area = self._side_a * self._side_b
        print(f'The area of quadrangle = {quard_area}')

    def perimetr(self):
        quard_per = (self._side_a + self._side_b) * 2
        print(f'Quadrangle perimetr = {quard_per}')


class Circle(Figura):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        circle_area = pi * self._radius ** 2
        print(f'Circle area = {circle_area}')

    def perimetr(self):
        circle_per = 2 * pi * self._radius
        print(f'Circle perimetr = {circle_per}')


class Triangle(Figura):
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def area(self):
        p = self.perimetr() / 2
        area_by_gero = sqrt(p * (p - self._side_a) * (p - self._side_b) * (p - self._side_c))
        print(f'Triangle area by Geron = {area_by_gero}')

    def perimetr(self):
        tria_per = self._side_a + self._side_b + self._side_c
        print(f'Triangle perimetr = {tria_per}')
        return tria_per

romb = Rhombus(5, 4)
chotyrykutnyk = Quadrangle(6, 13)
kolo = Circle(8)
trykutnyk = Triangle(5, 6, 7)

romb.area()
romb.perimetr()

chotyrykutnyk.area()
chotyrykutnyk.perimetr()

kolo.area()
kolo.perimetr()

trykutnyk.area()
trykutnyk.perimetr()