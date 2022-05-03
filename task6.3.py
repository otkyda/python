class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Profit' : wage, 'Bonus' : bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Bмя: {self.name} {self.surname}')

    def get_full_profit(self):
        print(f'Доход: {sum(self._income.values())}')

a = Position('Ivan', 'Ivanov', 'driver', 30000, 10000)
a.get_full_name()
a.get_full_profit()

