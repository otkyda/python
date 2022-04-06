my_list = [7, 5, 3, 3, 2]
new_count = int(input('Введите новый элемент рейтинга: '))

my_list.append(new_count)

print(sorted(my_list, reverse=True))
