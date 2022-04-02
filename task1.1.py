name_user = input("Введите имя пользователя: ")
profession_user = input("Введите профессию пользователя: ")
payment = float(input("Введите зарплату пользователя: "))
tax = payment*0.13
free_money = payment - tax
print(f"гражданин {name_user} по профессии {profession_user}")
print("При месячной зарплате {:.2f} подоходный налог составляет {:.2f}".format(payment, tax))
