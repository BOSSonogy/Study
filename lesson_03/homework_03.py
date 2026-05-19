# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland_1 = ('"Would you tell me, please, which way I ought to go from here?"'
                         '\n"That depends a good deal on where you want to get to," said the Cat.'
                         '\n"I don\'t much care where ——" said Alice.'
                         '\n"Then it doesn\'t matter which way you go," said the Cat.'
                         '\n"—— so long as I get somewhere," Alice added as an explanation.'
                         '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland_1)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area

print(f'Загальна площа Чорного та Азовського морів становий {total_area} квадратних кілометрів')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_sum = 375291
first_and_second = 250449
second_and_third = 222950
first = total_sum - second_and_third
third = total_sum - first_and_second
second = first_and_second - first

print(f'На 1-му складі {first} товарів, на 2-му складі {second} товарів, а на 3-му складі {third} товарів.')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

payments_duration = 18
payments_amount = 1179
computer_cost = payments_duration * payments_amount

print(f'Михайло разом з батьками заплатять {computer_cost} грн за покутку компʼютера')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f'Остачі від ділення чисел: a {a}, b {b}, c {c}, d {d}, e {e} та f {f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza = 4 * 274
medium_pizza = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_cost = large_pizza + medium_pizza + juice + cake + water

print(f'Для даного замовлення Іринці знадобиться {total_cost} грн')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photo_amount = 232
max_at_page = 8
pages = total_photo_amount // max_at_page

print(f'Ігорю знадобиться {pages} сторінок альбому, щоб вклеїти всі фото')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_consumption = 9
tank_capacity = 48
total_fuel_consumption = 1600//100 * 9
tank_refueling = total_fuel_consumption // tank_capacity

print(f'Для такої поїздки знадобиться {total_fuel_consumption} літри бензину')
print(f'Родині знадобиться заїхати на заправку щонайменше {tank_refueling} разів')
