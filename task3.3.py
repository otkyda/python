def my_func():
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = float(input('Введите третье число: '))
    except ValueError:
        print('Ошибка ввода данных')
    else:
        row = [a, b, c]
        row.sort()
        row.pop(0)
        sum_row = row[0] + row[1]
        print(sum_row)

my_func()
