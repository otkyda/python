from time import sleep
from colorama import Fore

class TrafficLight:
    __color = 'ВЫКЛЮЧЕН'

    def start(self):
        print(Fore.RED + 'КРАСНЫЙ')
        sleep(7)
        print(Fore.YELLOW + 'ЖЕЛТЫЙ')
        sleep(2)
        print(Fore.GREEN + 'ЗЕЛЕНЫЙ')
        sleep(5)


a = TrafficLight()
a.start()

