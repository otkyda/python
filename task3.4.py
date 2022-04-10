def my_func(x, y):
    result_1 = x**y
    idx = - 1
    result_2 = 1 / x
    while idx != y:
        result_2 = result_2 / x
        idx = idx - 1
    print(f'Результат определения в степень с помощью оператора "**" - {result_1}')
    print(f'Результат определения в степень с цикла - {result_2}')

x = -1
y = 1
while x <= 0:
    x = float(input('Введите действительное положительное число: '))
while y >= 0:
    y = int(input('Введите целое отрицательное число: '))

my_func(x, y)
