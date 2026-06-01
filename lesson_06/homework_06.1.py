
new_line = input('Введіть свою строку: ')
unique_symbol = []
count = 0

for i in new_line:
    if i not in unique_symbol:
        unique_symbol.append(i)
        count += 1
    else:
        continue

if count > 10:
    print('True')
else:
    print('False')