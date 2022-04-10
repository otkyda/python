def sum_count():
    count_1 = 0
    count_2 = 0
    sum_count = 0
    inp_data = 0

    while inp_data != '*':
        inp_data = str(input('Введите два числа через пробел. Для завершения введите * '))
        if inp_data == '*':
            break
        data_list = inp_data.split()
        if len(data_list) == 1:
            count_2 = 0
            try:
                count_1 = float(data_list[0])
            except ValueError:
                count_1 = 0
                count_2 = 0
                print('Ошибка ввода данных. Необходимо было вводить числа')
        if len(data_list) == 2:
            try:
                count_1 = float(data_list[0])
                count_2 = float(data_list[1])
            except ValueError:
                count_1 = 0
                count_2 = 0
                print('Ошибка ввода данных. Необходимо было вводить числа')
        if len(data_list) > 2:
            print('Символы введенные после второго пробела учитываться не будут')
            try:
                count_1 = float(data_list[0])
                count_2 = float(data_list[1])
            except ValueError:
                count_1 = 0
                count_2 = 0
                print('Ошибка ввода данных. Необходимо было вводить числа')
                break
        sum_count = sum_count + (count_1 + count_2)
        print(f'Cумма введенных чисел: {sum_count}')
    print(f'Итоговая сумма: {sum_count}')

sum_count()