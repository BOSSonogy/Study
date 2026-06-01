lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

def put_in(check_list):
    for i in check_list:
        if type(i) == str:
            lst2.append(i)

put_in(lst1)
print(lst2)