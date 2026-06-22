# перетворюєте їх у функції (якщо це потрібно)
# створіть в папці файл homeworks.py куди вставте ваші функції з дз
# та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
# імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
# На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.

def multiplication_table(number):
    multiplier = 1
    list_result = []

    while multiplier <= number:
        result = number * multiplier
        if  result > 25:
            break
        list_result.append(f"{number}x{multiplier}={result}")
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

    return list_result


multiplication_table(26)
print(multiplication_table(5))

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def put_in(check_list):
    lst2 = []
    for i in check_list:
        if type(i) == str:
            lst2.append(i)
    return lst2

print(put_in(lst1))



list_1 = [4, 7, 2, 9, 10, 44, 246, 359]

def counter(list1):
    even_sum = 0
    for i in list1:
        if i % 2 == 0:
            even_sum += i
        else:
            continue
    if even_sum >0:
        print(f'Сума парних чисел в списку = {even_sum}')
    else:
        print('В списку нема парних чисел')
    return even_sum

counter(list_1)

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