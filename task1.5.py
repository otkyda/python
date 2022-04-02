revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
profit = revenue - costs
profitability = round(profit / revenue, 2)

if profit > 0:
    print("Фирма получает прибыль")
    print(f"Рентабельность фирмы составляет: {profitability}")
    size_staff = int(input("Сообщите численность персонала: "))
    efect = round(profitability / size_staff, 2)
    print(f"Прибыль в пересчете на одного сотрудника составляет: {efect}")
elif profit == 0:
    print("Фирма не получает прибыли")
else:
    print("Фирма убыточна")
