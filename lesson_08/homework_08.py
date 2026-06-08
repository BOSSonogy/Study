class Student:
    def __init__(self, name, surname, age, ave_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.__grade = ave_grade

    def score_update(self, value):
        if isinstance(value, (int, float)):
            self.__grade = value
        else:
            raise ValueError("Incorrect average grade")


    def intro(self):
        print(f'{self.name} {self.surname}. He is {self.age}, and his average grade is {self.__grade}.')


student_1 = Student('John', 'Smith', 19, 68)
student_2 = Student('Bob', 'Ferrel', 22, 75.5)

student_1.intro()
student_2.intro()

student_2.score_update(79)
student_2.intro()
