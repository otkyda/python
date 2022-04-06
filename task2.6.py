el_name = None
position = None

num_1_list = []
num_2_list = []
num_3_list = []
num_4_list = []

position_list = ['название', 'цену', 'количество', 'ед. изм.']

print('Перечень №1')
for position in position_list :
    el_name = input(f'Введите {position} товара: ')
    num_1_list.append(el_name)

stat_1 = (1, {'Название': num_1_list[0], 'Цена': num_1_list[1], 'Количество': num_1_list[2], 'ед. изм.': num_1_list[3]})

print('Перечень №2')
for position in position_list :
    el_name = input(f'Введите {position} товара: ')
    num_2_list.append(el_name)

stat_2 = (2, {'Название': num_2_list[0], 'Цена': num_2_list[1], 'Количество': num_2_list[2], 'ед. изм.': num_2_list[3]})

print('Перечень №3')
for position in position_list :
    el_name = input(f'Введите {position} товара: ')
    num_3_list.append(el_name)

stat_3 = (3, {'Название': num_3_list[0], 'Цена': num_3_list[1], 'Количество': num_3_list[2], 'ед. изм.': num_3_list[3]})

print(stat_1)
print(stat_2)
print(stat_3)

#stat_1 = (1, {'Название': 'Компьютер', 'Цена': 30000, 'Количество': 7, 'ед. изм.': 'шт.'})
#stat_2 = (2, {'Название': 'Сканер', 'Цена': 10000, 'Количество': 2, 'ед. изм.': 'шт.'})
#stat_3 = (3, {'Название': 'Принтер', 'Цена': 15000, 'Количество': 9, 'ед. изм.': 'шт.'})

dict_1 = stat_1[1]
dict_2 = stat_2[1]
dict_3 = stat_3[1]

names = [dict_1['Название'], dict_2['Название'], dict_3['Название']]
names_dict = {'Название': names}

prices = [dict_1['Цена'], dict_2['Цена'], dict_3['Цена']]
prices_dict = {'Цена': prices}

quantity = [dict_1['Количество'], dict_2['Количество'], dict_3['Количество']]
quantity_dict = {'Цена': quantity}

units = [dict_1['ед. изм.'], dict_2['ед. изм.'], dict_3['ед. изм.']]
units_dict = {'Цена': units}

print(names_dict)
print(prices_dict)
print(quantity_dict)
print(units_dict)
