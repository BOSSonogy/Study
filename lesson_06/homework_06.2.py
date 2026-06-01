
def contain_it(word):
    count = 0
    word = input('Take a word: ')
    for k in word:
        if k == 'h' or k== 'H':
            print("Let's move next, You did it")
            count += 1
            break
        else:
            continue

    if count == 0:
        print('Try again')
        contain_it(None)


contain_it(None)
