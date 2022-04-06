some_list = []
len_some_list = 5
ind_some_list = 1

while ind_some_list <= len_some_list :
    el_list = input(f'Введите {ind_some_list}-й элемент списка: ')
    some_list.append(el_list)
    ind_some_list += 1

print(some_list)

some_list[0], some_list[1] = some_list[1], some_list[0]
some_list[3], some_list[4] = some_list[4], some_list[3]

print(some_list)