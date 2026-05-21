adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

update_1 = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""

update_2 = update_1.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

update_3 = " ".join(update_2.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(update_3.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print(sum(1 for word in update_3.split() if word[0].isupper()))


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first = update_3.index("Tom")
second = update_3.index("Tom", first + 1)

print(second)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = update_3.split(".") # Використав не оригінальну змінну з "....", а оновлену змінну

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for check in adwentures_of_tom_sawer_sentences:
    if check.startswith("By the time"):
        print('В тексті є речення, яке починається з "By the time"')
        break
else:
    print('В тексті немає речення, яке б починалось з "By the time"')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(len(adwentures_of_tom_sawer_sentences[-1].split()))
# print(len(adwentures_of_tom_sawer_sentences[-2].split())) # додатковий варіант враховуючи що останнє речення сформоване з крапки та пусте
