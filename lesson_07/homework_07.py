
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number: # Дана умова обмежує кількість ітерацій, як варіант я б використав "while multiplier > 0" для зняття такого обмеження
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sumer (first, second) -> None:
    result = first + second
    print(f'{first} + {second} = {result}')

num1 = int(input('Введіть 1-ше число: '))
num2 = int(input('Введіть 2-ге число: '))
sumer(num1, num2)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def list_arif(full_list) -> None:
    result = 0
    for i in full_list:
        result += i

    final_arif = result / len(full_list)
    print(f'Середнє арифметичне списку чисал {final_arif}')

list_1 = [3, 6, 1, 8, 3, 2, 29]

def list_gen() -> list:
    list2 = []
    count = 0
    number = int(input('Введи бажану кількість чисел у списку: '))
    while count < number:
        list2.append(int(input('Введи число: ')))
        count += 1
    return list2

new_list = list_gen()

list_arif(list_1)
list_arif(new_list)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def revers(line):
    new_line = line[::-1]
    print(new_line)

revers(input('Введи строку: '))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def row(listed) -> None:
    long = ''
    for i in listed:
        if len(i) > len(long):
            long = i
    print(f'Найдовше слово в списку: "{long}"')


word_list = input('Введіть бажані слова через кому: ').split(',')
row(word_list)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2) -> int:
    i = str1.find(str2)
    return i

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7

def find_it(line):
    unique_symbol = []
    count = 0

    for i in line:
        if i not in unique_symbol:
            unique_symbol.append(i)
            count += 1
        else:
            continue

    if count > 10:
        print('True')
    else:
        print('False')

find_it(input('Введіть свою строку: '))


# task 8

def finding():
    payments_duration = int(input('Скільки місяців необхідно виплачувати кредит? '))
    payments_amount = int(input('Яка сума платежу на місяць? '))
    computer_cost = payments_duration * payments_amount

    print(f'Михайло разом з батьками заплатять {computer_cost} грн за покутку компʼютера')

finding()


# task 9

def party():
    large_pizza = int(input('Скільки великої піцци буде на вечірці? ')) * int(input('Яка вартість 1-єї піцци? '))
    medium_pizza = int(input('Скільки середніх піцц буде на вечірці? ')) * int(input('Яка вартість 1-єї піцци? '))
    juice = int(input('Скільки соку буде на вечірці? ')) * int(input('Яка вартість 1-го соку? '))
    cake = int(input('Скільки тортів буде на вечірці? ')) * int(input('Яка вартість 1-го торта? '))
    water = int(input('Скільки пляшок фоди буде на вечірці? ')) * int(input('Яка вартість 1-єї пляшки? '))
    total_cost = large_pizza + medium_pizza + juice + cake + water
    print(f'Для даного замовлення на вечірку Іринці знадобиться {total_cost} грн')

party()


# task 10

def contain_it():
    word = input('Take a word: ')
    while 'h' not in word.lower():
        word = input("Try another word, it should contain 'h': ")
    else:
        print("Let's move next, You did it")

contain_it()


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""