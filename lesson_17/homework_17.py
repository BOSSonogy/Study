

def par_generate():
    n = int(input('До якого числа згенерувати послідовність парних чисел? '))
    for i in range(0, n + 1, 2):
        if i % 2 == 0:
            print(i)

par_generate()

def fibonacci(n):
    step = 0
    second = 1
    while step <= n:
        print(step)
        old_step = step
        step = second
        second = old_step + second

fibonacci(int(input('До якого числа згенерувати послідовність Фібоначі? ')))


def reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

my_list = ['Tried', 5, True, 26, 15, False]

back_gen = reverse(my_list)

for item in back_gen:
    print(item)

def par_iterator(n):
    step = 0
    while step <= n:
        yield step
        step += 2

N = int(input('До якого числа згенерувати парні числа? '))
for num in par_iterator(N):
    print(num)

def log_function(func):
    def wrapper(*args):
        print("Вхідні аргументи: ", args)
        result = func(*args)
        print("Результат функції: ", result)
        return result
    return wrapper


@log_function
def fibonacci(n):
    step = 0
    second = 1
    while step <= n:
        print(step)
        step, second = second, step + second
    return "Готово"


fibonacci(int(input('До якого числа згенерувати послідовність Фібоначчі? ')))

def catch_errors(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except Exception as error:
            print("Виникла помилка під час виконання: ", error)
            return None
    return wrapper

@catch_errors
def cached(n):
    step = 10
    while step >= 0:
        print(100 / step)
        step -= 2

cached(15)