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
        self.__side_a = side_a
        self.__height_h = height_h

    def area(self):
        return self.__side_a * self.__height_h
        #print(f'Rhombus area = {rhombus_area}')

    def perimetr(self):
        return self.__side_a * 4
        #print(f'Rhombus perimetr = {rhombus_per}')


class Quadrangle(Figura):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
        return self.__side_a * self.__side_b
        #print(f'The area of quadrangle = {quard_area}')

    def perimetr(self):
        return (self.__side_a + self.__side_b) * 2
        #print(f'Quadrangle perimetr = {quard_per}')


class Circle(Figura):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2
        #print(f'Circle area = {circle_area}')

    def perimetr(self):
        return 2 * pi * self.__radius
        #print(f'Circle perimetr = {circle_per}')


class Triangle(Figura):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        p = self.perimetr() / 2
        return sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))
        #print(f'Triangle area by Geron = {area_by_gero}')

    def perimetr(self):
        return self.__side_a + self.__side_b + self.__side_c
        #print(f'Triangle perimetr = {tria_per}')


figures = [
    Rhombus(6, 4),
    Quadrangle(8, 12),
    Circle(7),
    Triangle(7, 13, 16)
]

for figure in figures:
    print(f'Area = {figure.area()}')
    print(f'Perimeter = {figure.perimetr()}')
    print()



# romb = Rhombus(5, 4)
# chotyrykutnyk = Quadrangle(6, 13)
# kolo = Circle(8)
# trykutnyk = Triangle(5, 6, 7)
#
# romb.area()
# romb.perimetr()
#
# chotyrykutnyk.area()
# chotyrykutnyk.perimetr()
#
# kolo.area()
# kolo.perimetr()
#
# trykutnyk.area()
# trykutnyk.perimetr()