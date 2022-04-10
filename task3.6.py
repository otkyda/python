def int_func():
    check = False
    while check == False:
        inp_str = str(input('Введите слово, состояещее из маленьких латинских букв: '))
        str_list = inp_str.split()
        word = str_list[0]
        for letter in word:
            if letter >= 'a' and letter <= 'z':
                check = True
            else:
                check = False
        if check == True:
            print(str.title(word))
        else:
            print('Ошибка ввода')


int_func()



