result = float(input("Сообщите результат пробежки в первый день: "))
purpose = int(input("Сообщите какой результат необходим: "))
num_day = int(1)

if result >= purpose:
    print("Вы уже достигли результата")

while result <= purpose:
    result = round(result + (result * 0.1), 2)
    print(f"{num_day}-й день: {result}")
    num_day = num_day + 1

print(f"На {num_day}-й день Вы достигните результата {purpose}")