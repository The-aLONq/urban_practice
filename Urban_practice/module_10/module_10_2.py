import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.enemies > 0:
            if self.enemies <= 0:
                break
            self.enemies -= self.power
            self.day += 1

            print(f'{self.name} сражается {self.day} (кол-во дней), осталось {self.enemies} воинов.')
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

print('Все битвы закончились!')


