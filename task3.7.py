def int_func():
    check = False
    while check == False :
        inp_str = str(input('Введите разу, состоящую из маленьких латинских букв: '))
        for letter in inp_str:
            if letter >= 'a' and letter <= 'z':
                check = True
            else:
                check = False
        if check == True:
            print(str.title(inp_str))
        else:
            print('Ошибка ввода')


int_func()
