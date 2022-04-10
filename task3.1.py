def division():
    try:
        count_1 = float(input('Введите первое число: '))
        count_2 = float(input('Введите первое число: '))
        return count_1 / count_2
    except (ValueError, ZeroDivisionError):
        print('Ошибка ввода данных')

calc_1 = division()

while calc_1 == None:
    calc_1 = division()

print(calc_1)
