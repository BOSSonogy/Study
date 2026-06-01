# list_1 = list(map(int, input('Введи кілька чисел через кому: ').split(',')))
list_1 = [4, 7, 2, 9, 10, 44, 246, 359]

def counter(list1):
    even_sum = 0
    for i in list1:
        if i % 2 == 0:
            even_sum += i
        else:
            continue
    if even_sum >0:
        print(f'Сума парних лисел в списку = {even_sum}')
    else:
        print('В списку нема парних чисел')

counter(list_1)