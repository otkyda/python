num = int(input('Введите номер месяца: '))
if num < 1 or num > 12 :
  print('Некорректное значение')
  num = int(input('Введите номер месяца: '))
  
season = {12 : 'winter', 1 : 'winter' , 2 : 'winter' , 3 : 'spring', 4 : 'spring', 
5 : 'spring', 6 : 'summer', 7 : 'summer', 8 : 'summer' , 9 : 'autumn', 10 : 'autumn', 11 : 'autumn'}

print(season.get(num))