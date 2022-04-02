user_count = 0
while user_count < 1 or user_count > 9:
    user_count = int(input("Введите цифру от 1 до 9: "))
counting = user_count + (user_count * 10 + user_count) + ((user_count * 100) + (user_count * 10) + user_count)
print(counting)